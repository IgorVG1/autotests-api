import allure

from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true
from tools.logger import get_logger

# Создаем логгер с именем "AUTHENTICATION_ASSERTIONS"
logger = get_logger("AUTHENTICATION_ASSERTIONS")


@allure.step("Check success authentication user response")
def assert_login_response(response: LoginResponseSchema) -> None:
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    logger.info('Check success authentication user response')
    assert_equal(actual=response.token.token_type, expected='bearer', name='token_type')
    assert_is_true(actual=response.token.access_token,  name='access_token')
    assert_is_true(actual=response.token.refresh_token, name='refresh_token')