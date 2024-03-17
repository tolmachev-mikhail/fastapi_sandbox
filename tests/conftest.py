from dotenv import load_dotenv
from fastapi.testclient import TestClient
from pytest import fixture

from main import app
from settings import ENV_PATH

load_dotenv(ENV_PATH)


@fixture
def client():
    return TestClient(app)
