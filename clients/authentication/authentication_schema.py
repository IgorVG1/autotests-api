from pydantic import BaseModel, Field, EmailStr, ConfigDict
from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    Attributes:
        token_type: str (tokenType)
        access_token: str (accessToken)
        refresh_token: str (refreshToken)
    """
    model_config = ConfigDict(populate_by_name=True)

    token_type: str     = Field(alias="tokenType")
    access_token: str   = Field(alias="accessToken")
    refresh_token: str  = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    Attributes:
        email: str
        password: str
    """
    email: EmailStr = Field(default_factory=fake.email)
    password: str   = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    Attributes:
        token: TokenSchema
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    Attributes:
        refresh_token: str (refreshToken)
    """
    model_config = ConfigDict(populate_by_name=True)
    # для негативного тестирования генерируем случайное значение по умолчанию
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)