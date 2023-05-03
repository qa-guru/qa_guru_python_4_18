import os
from model.demoshop import Demoshop
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')
API_URL = os.getenv('api_url')
WEB_URL = os.getenv('web_url')


def test_demoshop(demoqashop_session):
    demoqashop_session.post(url="/addproducttocart/catalog/31/1/1")
    response = demoqashop_session.post(url="/addproducttocart/catalog/31/1/1")

    assert response.json()["success"] is True
    assert response.json()["updatetopcartsectionhtml"] == "(2)"


def test_demoshop_with_object_model(demoqashop_session):
    demoshop = Demoshop(demoqashop_session)

    demoshop.add_to_cart()
    cart = demoshop.add_to_cart()

    assert cart.addition_success_status is True
    assert cart.products_count == "(2)"


def test_demoshop_with_object_model_additional_product():
    demoshop = Demoshop().login(LOGIN, PASSWORD)

    demoshop.add_to_cart(product_id="43/1/1")
    cart = demoshop.add_to_cart(product_id="43/1/1")

    assert cart.addition_success_status is True
    assert cart.products_count == "(2)"
