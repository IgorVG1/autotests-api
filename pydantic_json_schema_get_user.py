from tools.fakers import Tools
from tools.assertions.schema import validate_json_schema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from clients.users.private_users_client import get_private_users_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.users_schema import GetUserResponseSchema

# Инициализируем публичный клиент
public_users_clients = get_public_users_client()

# Создаем нового пользователя
create_user_request = CreateUserRequestSchema(
    email=Tools().get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_users_clients.create_user(create_user_request)

# Инициализируем приватный клиент
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

private_users_clients = get_private_users_client(authentication_user)

# Выполняем запрос на получение данных о созданном пользователе с использованием метода API клиента
get_user_api_response = private_users_clients.get_user_api(user_id=create_user_response.user.id)
get_user_api_schema = GetUserResponseSchema.model_json_schema()

# Валидируем JSON schema ответа эндпоинта
validate_json_schema(get_user_api_response.json(), get_user_api_schema)
print("All good")