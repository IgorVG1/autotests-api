import httpx
import pprint
from tools.fakers import fake

# Create User
username = fake.email()
create_user_payload = {
    "email": username,
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post(url="http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
create_user_response_status = create_user_response.status_code
print('\n'+'='*100)
print('ПОЛЬЗОВАТЕЛЬ УСПЕШНО СОЗДАН')
print('-'*100)
print(f'URL: {create_user_response.url}')
print(f'Status Code: {create_user_response_status}')
print('Response: ')
print('-'*100)
pprint.pprint(create_user_response_data)
print('='*100)


# Autentification
login_payload = {
    "email": username,
    "password": "string"
}
login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
login_response_status = login_response.status_code
print('ПОЛЬЗОВАТЕЛЬ УСПЕШНО АУТЕНТИФИЦИРОВАН')
print('-'*100)
print(f'URL: {login_response.url}')
print(f'Status Code: {login_response_status}')
print('Response: ')
print('-'*100)
pprint.pprint(login_response_data)
print('='*100)


# Upload file
create_file_head = {
    "Authorization": f'Bearer {login_response_data['token']['accessToken']}'
}
create_file_payload = {
    "filename": "image.jpg",
    "directory": "courses"
}
create_file_response = httpx.post(url="http://localhost:8000/api/v1/files",
                                  headers=create_file_head,
                                  data=create_file_payload,
                                  files={"upload_file": open('testdata//files//image.jpg', 'rb')})
create_file_response_data = create_file_response.json()
create_file_response_status = create_file_response.status_code
print('ФАЙЛ УСПЕШНО ЗАГРУЖЕН НА СЕРВЕР')
print('-'*100)
print(f'URL: {create_file_response.url}')
print(f'Status Code: {create_file_response_status}')
print('Response: ')
print('-'*100)
pprint.pprint(create_file_response_data)
print('='*100)