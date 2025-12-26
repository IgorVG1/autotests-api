import httpx
import allure

from http import HTTPStatus
from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal, assert_status_code
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # Формируем ожидаемую ссылку на загруженный файл
    expected_url = f'http://localhost:8000/static/{request.directory}/{request.filename}'

    assert_equal(str(response.file.url), expected_url, 'url')
    assert_equal(response.file.filename, request.filename, 'filename')
    assert_equal(response.file.directory, request.directory, 'directory')


@allure.step("Check file is accessible in {url}")
def assert_file_is_accessible(url: str):
    """
    Проверяет, что файл доступен по указанному URL.

    :param url: Ссылка на файл.
    :raises AssertionError: Если файл не доступен.
    """
    response = httpx.get(url)
    assert_status_code(response.status_code, HTTPStatus.OK)


@allure.step("Check structure File-object")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.url, expected.url, 'url')
    assert_equal(actual.directory, expected.directory, 'directory')
    assert_equal(actual.filename, expected.filename, 'filename')


@allure.step("Check get file response")
def assert_get_file_response(get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание.

    :param get_file_response: Ответ API при запросе данных файла.
    :param create_file_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_file(get_file_response.file, create_file_response.file)


@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                loc=["body","filename"],
                msg="String should have at least 1 character",
                input="",                                       # Пустое имя файла (Негативное тестирование)
                ctx={"min_length":1}
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                loc=["body","directory"],
                msg="String should have at least 1 character",
                input="",                                       # Пустая директория (Негативное тестирование)
                ctx={"min_length":1}
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(detail="File not found")
    assert_internal_error_response(actual, expected)


@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ API на запрос файла с некорректным file_id
    соответствует ожидаемому формату ошибки валидации.

    :param actual: Фактический ответ API с ошибкой валидации
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому
    """
    expected = ValidationErrorResponseSchema(
        dateils=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={
                    "error":    "invalid character: expected an optional prefix of `urn:uuid:` "
                                "followed by [0-9a-fA-F-], found `i` at 1"
                },
                message="Input should be a valid UUID, invalid character: "
                        "expected an optional prefix of `urn:uuid:` "
                        "followed by [0-9a-fA-F-], found `i` at 1",
                location=["path", "file_id"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)