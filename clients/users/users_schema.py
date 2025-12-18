from pydantic import BaseModel, Field, EmailStr, ConfigDict
from tools.fakers import fake



# PydanticModels для private_users_client.py

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    Attributes:
        id: str
        email: str
        last_name: str (lastName)
        first_name: str (firstName)
        middle_name: str (middleName)
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str   = Field(alias="lastName")
    first_name: str  = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    Attributes:
        email: str
        last_name: str (lastName)
        first_name: str (firstName)
        middle_name: str (middleName)
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None  = Field(default_factory=fake.email)
    last_name: str | None   = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None  = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)



# PydanticModels для public_users_client.py

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    Attributes:
        email: str
        password: str
        last_name: str (lastName)
        first_name: str (firstName)
        middle_name: str (middleName)
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr     = Field(default_factory=fake.email)
    password: str       = Field(default_factory=fake.password)
    last_name: str      = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str     = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str    = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema