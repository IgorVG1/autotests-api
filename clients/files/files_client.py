from httpx import Response
from clients.api_client import APIClient
from clients.files.files_schema import *
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema



class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def get_file(self, file_id: str) -> GetFileResponseSchema:
        """
        Метод, который будет запрашивать информацию о файле и возвращать JSON-структуру
        """
        response = self.get_file_api(file_id)
        return GetFileResponseSchema.model_validate_json(response.text)

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/files",
                         data=request.model_dump(),
                         files={"upload_file": open(request.upload_file, 'rb')})

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Метод, который будет загружать файл и возвращать JSON-структуру
        """
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")


# Добавляем builder для FilesClient
def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))