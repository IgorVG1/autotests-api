from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.location, expected.location, "location")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")


def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


def assert_internal_error_response(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equal(actual.detail, expected.detail, "detail")


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(detail="File not found")
    assert_internal_error_response(actual,expected)

def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ API на запрос файла с некорректным file_id
    соответствует ожидаемому формату ошибки валидации.

    :param actual: Фактический ответ API с ошибкой валидации
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                ctx={"error":   "invalid character: expected an optional prefix of `urn:uuid:` "
                                "followed by [0-9a-fA-F-], found `i` at 1"},
                msg="Input should be a valid UUID, invalid character: "
                    "expected an optional prefix of `urn:uuid:` "
                    "followed by [0-9a-fA-F-], found `i` at 1",
                loc=["path","file_id"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)