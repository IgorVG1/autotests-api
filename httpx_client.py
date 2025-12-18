import httpx
import pprint

from tools.fakers import fake

# Генерируем почту для пользователя
username = fake.email()
print(f'Сгенерирована новая почта:      {username}')

# Создаем пользователя
response_create_user = httpx.post(url="http://localhost:8000/api/v1/users", json={
    "email": username,
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
})
print(f'Создан пользователь с почтой:   {username}')

# Аутентифицируемся
response_log_in = httpx.post(url='http://localhost:8000/api/v1/authentication/login',json={
    "email": username,
    "password": "string"
})
print('Пользователь успешно вошел в систему')

# Инициируем клиент
client = httpx.Client(base_url="http://localhost:8000",
                      headers={"Authorization": f"Bearer {response_log_in.json()['token']['accessToken']}"})

# Выполняем GET-запрос, используя клиент
response = client.get("/api/v1/users/me")

# Выводим ответ в консоль
print("="*100)
print(response.status_code)
print(response.url)
print("-"*100)
pprint.pprint(response.json())
print("="*100)