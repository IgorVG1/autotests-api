import allure

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=response.user.email,        expected=request.email,         name='email')
    assert_equal(actual=response.user.last_name,    expected=request.last_name,     name='last_name')
    assert_equal(actual=response.user.first_name,   expected=request.first_name,    name='first_name')
    assert_equal(actual=response.user.middle_name,  expected=request.middle_name,   name='middle_name')


@allure.step("Check structure User-object")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что фактические данные пользователя соответствуют ожидаемым.

    :param actual: Фактические данные пользователя.
    :param expected: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.id,          expected=expected.id,           name='id')
    assert_equal(actual=actual.email,       expected=expected.email,        name='email')
    assert_equal(actual=actual.last_name,   expected=expected.last_name,    name='last_name')
    assert_equal(actual=actual.first_name,  expected=expected.first_name,   name='first_name')
    assert_equal(actual=actual.middle_name, expected=expected.middle_name,  name='middle_name')


@allure.step("Check get user response")
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на его создание.

    :param get_user_response: Ответ API при запросе данных пользователя.
    :param create_user_response: Ответ API при создании пользователя.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    assert_user(get_user_response.user, create_user_response.user)