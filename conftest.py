import os

import pytest
from dotenv import load_dotenv

from hosts import HOSTS
from utils.helper import BaseSession

load_dotenv()

LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')
API_URL = os.getenv('api_url')
WEB_URL = os.getenv('web_url')


def pytest_addoption(parser):
    parser.addoption("--stage")


@pytest.fixture(scope="session")
def reqres():
    with BaseSession(base_url="https://reqres.in/api") as session:
        yield session


@pytest.fixture(scope="session")
def ninja_cats():
    with BaseSession(base_url="https://api.api-ninjas.com/v1/cats") as session:
        session.headers = {"X-Api-Key": "auth_token"}
        yield session


@pytest.fixture(scope="session")
def reqres(request):
    stage = request.config.getoption("--stage")
    url = HOSTS["reqres"][stage]

    with BaseSession(base_url=url) as session:
        yield session


@pytest.fixture(scope="session")
def demoqashop_session(request):
    stage = request.config.getoption("--stage")
    url = HOSTS["API"][stage]
    with BaseSession(base_url=url) as session:
        auth_cookie_name = "NOPCOMMERCE.AUTH"
        response = session.post(
            url='/login',
            data={'Email': LOGIN, 'Password': PASSWORD},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )
        auth_cookie = response.cookies.get(auth_cookie_name)
        session.cookies.set(auth_cookie_name, auth_cookie)
        yield session
