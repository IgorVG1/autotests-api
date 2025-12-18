import httpx
import pprint

base_url = 'http://localhost:8000/api/v1'
username = "mail4@mail.com"
password = "1221"


class Users:
    def __init__(self):
        self.username = username
        self.password = password
        self.last_name = "QA"
        self.first_name = "Igor"
        self.middle_name = "Tester"


    def test_post_create_user(self):

        link = '/users'
        payload = {
            "email": self.username,
            "password": self.password,
            "lastName": self.last_name,
            "firstName": self.first_name,
            "middleName": self.middle_name
        }

        response = httpx.post(url=base_url+link, json=payload)
        response_json = response.json()

        print(f'\nStatus code: {response.status_code}')
        print(f'URL: {response.url}')
        pprint.pprint(response.json())

        return response_json


class Authentication:
    def __init__(self):
        self.username = username
        self.password = password

    def test_post_login(self) -> dict:

        link = '/authentication/login'
        payload = {
            "email": username,
            "password": password
        }

        response = httpx.post(url=base_url+link, json=payload)
        response_json = response.json()

        # print(f'\nStatus code: {response.status_code}')
        # print(f'URL: {response.url}')
        # pprint.pprint(response.json())

        return response_json

    def get_access_token(self) -> str:
        token_json = Authentication().test_post_login()
        access_token = token_json['token']['accessToken']
        token_type = token_json['token']['tokenType'].capitalize()

        print(f'\nAccess Token: {token_type} {access_token}')
        return access_token

    def get_refresh_token(self) -> str:
        token_json = Authentication().test_post_login()
        refresh_token = token_json['token']['refreshToken']
        token_type = token_json['token']['tokenType'].capitalize()

        print(f'\nRefresh Token: {token_type} {refresh_token}')
        return refresh_token

    def test_post_refresh(self) -> dict:
        link = '/authentication/refresh'
        payload = {"refreshToken": Authentication().get_refresh_token()}

        response = httpx.post(url=base_url+link, json=payload)
        response_json = response.json()

        print(f'\nStatus code: {response.status_code}')
        print(f'URL: {response.url}')
        pprint.pprint(response.json())

        return response_json