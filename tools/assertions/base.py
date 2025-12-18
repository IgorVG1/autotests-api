from typing import Any

def assert_status_code(actual: int, expected: int) -> None:
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, \
        (
            'Incorrect response status code.'
            f'\nExpected status code:   {expected}'
            f'Actual status code:       {actual}'
        )

def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, \
        (
            f'Incorrect value: "{name}"'
            f'\nExpected value: {expected}'
            f'Actual value:     {actual}'
        )

def assert_is_true(actual: Any, name: str) -> None:
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raise
    """
    assert actual, \
        (
            f'Incorrect value: "{name}"'
            f'\nExpected true value, but actual: {actual}'
        )