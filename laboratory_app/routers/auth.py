import logging
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from traceback import format_exc
from typing import Annotated

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import (OAuth2PasswordBearer, OAuth2PasswordRequestForm,
                              SecurityScopes)
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, ValidationError

from laboratory_app.enums import AuthScopes, JobTitle
from laboratory_app.models import Employee, Registry
from laboratory_app.utils import db_dependency

logger = logging.getLogger(__name__)

load_dotenv(Path(__file__).parent / ".env")

SECRET_KEY = os.environ.get("SECRET_KEY", "")
ALGO = os.environ.get("ALGO", "")

if SECRET_KEY == "" or ALGO == "":
    raise EnvironmentError("Authentication parameters are not configured")

ACCESS_TOKEN_EXPIRE_MINUTES = 30

AUTH_SCOPES_MAPPING = {
    JobTitle.DOCTOR: [AuthScopes.EMPLOYEE, AuthScopes.DOCTOR],
    JobTitle.REGISTAR: [AuthScopes.EMPLOYEE, AuthScopes.REGISTAR],
    JobTitle.LABORANT: [AuthScopes.EMPLOYEE],
}


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
    scopes={
        AuthScopes.EMPLOYEE: "Read access about any patient and analysis",
        AuthScopes.DOCTOR: "Read/Write access to any analysis results",
        AuthScopes.REGISTAR: "Read/Write access to registaration",
    },
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)
    return encoded_jwt


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr
    scopes: list


class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


async def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: db_dependency,
) -> User:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
        email = payload.get("sub")
        if not email:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(email=email, scopes=token_scopes)
    except (JWTError, ValidationError) as e:
        logger.error(f"Error with provided token: {e} {format_exc()}")
        raise credentials_exception
    if token_data.email.endswith("lab.com"):
        logger.debug("Trying to find user in employee database")
        user = db.query(Employee).filter(Employee.email == token_data.email).first()
    else:
        logger.debug("Trying to find user in patient database")
        user = db.query(Registry).filter(Registry.email == token_data.email).first()
    if not user:
        logger.error(f"No patient/employee was found for {token_data.email}")
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return User(email=user.email, first_name=user.first_name, last_name=user.last_name)  # type: ignore[arg-type]


@router.post("/token", status_code=status.HTTP_200_OK)
def login_for_auth_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
) -> Token:
    if form_data.username.endswith("lab.com"):
        logger.debug("Trying to find user in employee database")
        user = db.query(Employee).filter(Employee.email == form_data.username).first()
    else:
        logger.debug("Trying to find user in patient database")
        user = db.query(Registry).filter(Registry.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    available_scopes = (
        AUTH_SCOPES_MAPPING[user.job_title]
        if form_data.username.endswith("lab.com")
        else []
    )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.email,
            "scopes": [
                scope for scope in form_data.scopes if scope in available_scopes
            ],
        },
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")
