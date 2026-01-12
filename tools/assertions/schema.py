import allure

from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
from tools.logger import get_logger

# Создаем логгер с именем "SCHEMA_ASSERTIONS"
logger = get_logger("SCHEMA_ASSERTIONS")


@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: Any) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    logger.info('Validate JSON schema')
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )

"""Разбираем код

1.  Функция validate_json_schema принимает два аргумента:
    -   instance: dict — JSON-объект, который возвращает API.
    -   schema: dict — JSON-schema, описывающая ожидаемую структуру.
    
2.  Вызывает validate() для проверки соответствия.

3.  Если instance не соответствует schema, выбрасывается jsonschema.exceptions.ValidationError.
    -   Это позволит тестам сразу выявлять ошибки в ответах API.
    
4.  format_checker=Draft202012Validator.FORMAT_CHECKER позволяет валидировать строки на соответствие формату, например, проверку email или URL.
    -   Если в ответе будет некорректное значение, например, неправильный формат email, это вызовет ошибку валидации.
"""