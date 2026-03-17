import logging

import requests


class BaseClient(object):
    """
    Базовый класс для API клиентов.
    Оборачивает requests.Session и управляет базовыми URL.
    """
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self, method, endpoint, **kwargs):
        """
        Внутренний (приватный) метод для выполнения запроса.
        Он склеивает базовый URL и конкретный эндпоинт.
        """
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint

        url = f"{self.base_url}{endpoint}"

        logging.getLogger(__name__).debug(
            f"-- Request: {method} {url} --"
        )

        response = self.session.request(method=method, url=url, **kwargs)
        return response

    def get(self, endpoint, **kwargs):
        """Выполняет GET запрос"""
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """Выполняет POST запрос"""
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """Выполняет PUT запрос"""
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        """Выполняет DELETE запрос"""
        return self._request("DELETE", endpoint, **kwargs)
