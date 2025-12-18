import pprint, jsonschema

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import *
from tools.assertions.schema import validate_json_schema
from tools.fakers import Tools

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=Tools().get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
# Получаем JSON-ответ от сервера через API
create_user_response = public_users_client.create_user_api(create_user_request).json()
# Получаем JSON-схему из Pydantic-модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

# Проверяем, что JSON-ответ от API соответствует ожидаемой JSON-схеме
validate_json_schema(create_user_response, create_user_response_schema)