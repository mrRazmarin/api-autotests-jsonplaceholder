import logging

import pytest

from api.posts import PostClient
from config.settings import BASE_URL


@pytest.fixture(scope="function")
def posts_client():
    """
    Фикстура, которая создает экземпляр клиента для работы с постами.
    scope="function" означает, что клиент создается заново для каждого теста.
    """

    logging.getLogger(__name__).debug(
        f"-- Create API client --"
    )

    client = PostClient(BASE_URL)
    yield client
    logging.getLogger(__name__).debug(
        f"-- API client is deleted --"
    )