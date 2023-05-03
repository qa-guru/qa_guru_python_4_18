import os

from dotenv import load_dotenv

from model.cart import Cart
from utils.helper import BaseSession

load_dotenv()


class Demoshop:
    def __init__(self):
        self.demoqa = BaseSession(base_url=os.getenv('api_url'))
        self.cart = None
        self.__add_to_cart_url_part = "/addproducttocart/catalog"

    def login(self, email, password):
        auth_cookie_name = "NOPCOMMERCE.AUTH"
        response = self.demoqa.post(
            url='/login',
            data={'Email': email, 'Password': password},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )
        auth_cookie = response.cookies.get(auth_cookie_name)
        self.demoqa.cookies.set(auth_cookie_name, auth_cookie)
        return self

    def add_to_cart(self, product_id="31/1/1"):
        self.cart = Cart(json=self.demoqa.post(url=f"{self.__add_to_cart_url_part}/{product_id}").json())
        return self.cart
