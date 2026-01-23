import allure

from typing import Any

from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles



class APIClient:
    def __init__(self, client: Client) -> None:
        self.client = client


    @allure.step("Make GET-request to {url}")
    def get(self,
            url: URL | str,
            params: QueryParams | None = None
            ) -> Response:
        return self.client.get(url=url, params=params)
    """
    Выполняет GET-запрос.
    
    :param url: URL-адрес эндпоинта.
    :param params: GET-параметры запроса (например, ?key=value).
    :return: Объект Response с данными ответа.
    """


    @allure.step("Make POST-request to {url}")
    def post(self,
             url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        return self.client.post(url=url, json=json, data=data, files=files)
    """
    Выполняет POST-запрос.
    
    :param url: URL-адрес эндпоинта.
    :param json: Данные в формате JSON.
    :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
    :param files: Файлы для загрузки на сервер.
    :return: Объект Response с данными ответа.
    """


    @allure.step("Make PATCH-request to {url}")
    def patch(self,
              url: URL | str,
              json: Any | None = None
              ) -> Response:
        return self.client.patch(url=url, json=json)
    """
    Выполняет PATCH-запрос (частичное обновление данных).

    :param url: URL-адрес эндпоинта.
    :param json: Данные для обновления в формате JSON.
    :return: Объект Response с данными ответа.
    """


    @allure.step("Make DELETE-request to {url}")
    def delete(self,
               url: URL | str
               ) -> Response:
        return self.client.delete(url=url)
    """
    Выполняет DELETE-запрос (удаление данных).

    :param url: URL-адрес эндпоинта.
    :return: Объект Response с данными ответа.
    """