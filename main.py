from fastapi import FastAPI

from laboratory_app.routers import laboratory_router

app = FastAPI()

app.include_router(laboratory_router)
