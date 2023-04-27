import logging

import curlify
from allure import step
from requests import Session, Response


def console_logger(function):
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        logging.info(curlify.to_curl(response.request))
        logging.info(response.text)
        return response
    return wrapper


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @console_logger
    def request(self, method, url, **kwargs):
        with step(f'{method} {url}'):
            response = super().request(method=method, url=f'{self.base_url}{url}', **kwargs)
            # logging.info(curlify.to_curl(response.request))
            # logging.info(response.text)
        return response
