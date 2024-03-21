import json
import os

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from pytest import fixture

from laboratory_app.enums import AuthScopes
from main import app
from settings import ENV_PATH

load_dotenv(ENV_PATH)

def get_auth_headers(client, username:str, password: str, scope:str):
    data = {
        "grant_type": "",
        "username": username,
        "password": password,
        "scope": scope,
        "client_id": "",
        "client_secret": "",
    }
    response = client.post("/auth/token", data=data)
    content = json.loads(response.content)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {content["access_token"]}"
    }
    return headers


@fixture(scope="session")
def client():
    return TestClient(app)

@fixture(scope="session")
def doctor_auth_headers(client):
    return get_auth_headers(client, username=os.getenv("SYS_TST_DOCTOR"),
                            password=os.getenv("SYS_TST_DOCTOR_PASSWORD"),
                            scope=f"{AuthScopes.EMPLOYEE} {AuthScopes.DOCTOR}")

@fixture(scope="session")
def laborant_auth_headers(client):
    return get_auth_headers(client, username=os.getenv("SYS_TST_LABORANT"),
                            password=os.getenv("SYS_TST_LABORANT_PASSWORD"),
                            scope=f"{AuthScopes.EMPLOYEE}")

@fixture(scope="session")
def registar_auth_headers(client):
    return get_auth_headers(client, username=os.getenv("SYS_TST_REGISTAR"),
                            password=os.getenv("SYS_TST_REGISTAR_PASSWORD"),
                            scope=f"{AuthScopes.EMPLOYEE} {AuthScopes.REGISTAR}")
