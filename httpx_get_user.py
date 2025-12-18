import httpx
import pprint

from tools.fakers import fake

url_create_user = 'http://localhost:8000/api/v1/users'
url_login = 'http://localhost:8000/api/v1/authentication/login'
url_get_user = 'http://localhost:8000/api/v1/users'
url_get_me = 'http://localhost:8000/api/v1/users/me'

email_user = fake.email()   # Создаем email для нового пользователя

data_create_user = {
    "email": email_user,
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"}

data_login = {
    "email": email_user,
    "password": "string"}

# Шаг 1. Создаем пользователя
response_create_user = httpx.post(url_create_user, json=data_create_user)

user_id = response_create_user.json()["user"]["id"]     # Сохраняем id пользователя

print()
print('='*100)
print(f'Endpoint: {response_create_user.url}')
print(f'Создан пользователь с email: {email_user}')
print(f'ID пользователя: {user_id}')
print(f'Статус код ответа: {response_create_user.status_code}')
pprint.pprint(response_create_user.json())

# Шаг 2. Проходим аутентификацию
response_login = httpx.post(url_login, json=data_login)

token_access = response_login.json()["token"]["accessToken"]    # Сохраняем access_token

print('='*100)
print(f'Endpoint: {response_login.url}')
print(f'Аутентифицирован пользователь с email: {email_user}')
print(f'Статус код ответа: {response_login.status_code}')
pprint.pprint(response_login.json())

# Шаг 3.1 Получаем данные пользователя
head_get_user = {"Authorization": f"Bearer {token_access}"}

response_get_user = httpx.get(url=f'{url_get_user}/{user_id}', headers=head_get_user)

print('='*100)
print(f'Endpoint: {response_get_user.url}')
print(f'Статус код ответа: {response_get_user.status_code}')
pprint.pprint(response_get_user.json())

# Шаг 3.2 Получаем данные пользователя
head_get_me = {"Authorization": f"Bearer {token_access}"}

response_get_me = httpx.get(url=url_get_me, headers=head_get_me)

print('='*100)
print(f'Endpoint: {response_get_me.url}')
print(f'Статус код ответа: {response_get_me.status_code}')
pprint.pprint(response_get_me.json())