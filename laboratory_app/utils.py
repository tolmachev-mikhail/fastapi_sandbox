import logging
from traceback import format_exc
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from database import SessionLocal

logger = logging.getLogger(__name__)


def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        logger.error(f"Can't create a session with error {e} {format_exc()}")
        raise
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
