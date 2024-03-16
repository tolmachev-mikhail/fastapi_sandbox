from fastapi import FastAPI

import models
from database import engine
from laboratory_app.routers import (
    authenication_router,
    laboratory_router,
    registry_router,
)

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authenication_router)
app.include_router(registry_router)
app.include_router(laboratory_router)
