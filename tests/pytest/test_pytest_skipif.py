import pytest


# Для примера укажем версию тестируемой системы
SYSTEM_VERSION = "v1.2.0"



# Пропустим тест, если версия системы равна v1.3.0
@pytest.mark.skipif(
    condition=(SYSTEM_VERSION == "v1.3.0"),
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():    # В текущей конфигурации этот тест запустится
    pass

# Пропустим тест, если версия системы равна v1.2.0
@pytest.mark.skipif(
    condition=(SYSTEM_VERSION == "v1.2.0"),
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():  # Этот тест не запустится
    pass