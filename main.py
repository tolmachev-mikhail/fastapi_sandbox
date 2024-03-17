from fastapi import FastAPI

from laboratory_app.routers import (authenication_router, laboratory_router,
                                    registry_router)

app = FastAPI()

app.include_router(authenication_router)
app.include_router(registry_router)
app.include_router(laboratory_router)
