from typing import Annotated

from fastapi import APIRouter, Security, status

from laboratory_app.enums import AuthScopes

from .auth import User, get_current_user

router = APIRouter(prefix="/laboratory", tags=["Laboratory"])


@router.post("/analysis", status_code=status.HTTP_201_CREATED)
async def order_laboratory_analysis(
    user: Annotated[User, Security(get_current_user, scopes=[AuthScopes.REGISTAR])]
):
    return "Analysis ordered"


@router.get("/analysis/{id}", status_code=status.HTTP_200_OK)
async def receive_analysis_result(
    id,
    user: Annotated[
        User,
        Security(
            get_current_user,
        ),
    ],
):
    pass


@router.patch("/analysis/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_analysis_info(
    id, user: Annotated[User, Security(get_current_user, scopes=[AuthScopes.DOCTOR])]
):
    return "Analysis updated"
