from functools import lru_cache

from pydantic import BaseModel, EmailStr, ConfigDict
from httpx import Client
from clients.authentication.authentication_client import get_authentication_client, LoginRequestSchema
from clients.event_hooks import curl_event_hook


class AuthenticationUserSchema(BaseModel):
    """
    Структура данных пользователя для авторизации
    Attributes:
        email: str
        password: str
    """
    model_config = ConfigDict(frozen=True)

    email: EmailStr
    password: str


@lru_cache(maxsize=None)    # Кешируем возвращаемое значение
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()
    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestSchema(email=user.email,
                                       password=user.password)
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        event_hooks={"request": [curl_event_hook]},
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )