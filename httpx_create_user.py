import httpx
import pprint
from tools.fakers import fake

url = 'http://localhost:8000/api/v1/users'

data = {
    "email": fake.email(),  # Используем функцию для генерации случайного email
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response = httpx.post(url=url, json=data)

print(f'\nEndpoint: {response.url}')
print(f'Создан пользователь с email: {response.json()["user"]["email"]}')
print(f'Статус код ответа: {response.status_code}')
pprint.pprint(response.json())