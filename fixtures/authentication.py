import pytest

from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client


@pytest.fixture(scope='function')
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()