import os

import pytest
import requests

from utils.helper import BaseSession


@pytest.fixture(scope="session")
def reqres():
    with BaseSession(base_url="https://reqres.in/api") as session:
        yield session


@pytest.fixture(scope="session")
def ninja_cats():
    with BaseSession(base_url="https://api.api-ninjas.com/v1/cats") as session:
        session.headers = {"X-Api-Key": "auth_token"}
        yield session
