from pydantic import BaseModel, Field





# 2. Создание базовой модели
"""Рассмотрим следующий JSON-объект, который нам нужно описать с помощью Pydantic:
{
  "id": "string",
  "title": "string",
  "maxScore": 0,
  "minScore": 0,
  "description": "string",
  "estimatedTime": "string"
}

Для описания такой структуры создадим Pydantic-модель: 
"""
class CourseSchema(BaseModel):
    """Course Schema.

    :param 1: id
    :type 1: str
    :param 2: title
    :type 1: str
    :param 3: maxScore
    :type 2: int
    :param 4: minScore
    :type 2: int
    :param 5: description
    :type 1: str
    :param 6: estimatedTime
    :type 1: str
    """
    id: str
    title: str
    max_score: int = Field(alias='maxScore', default=100)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "Пустое описание курса"
    estimated_time: str = Field(alias='estimatedTime')






# 3. Инициализация модели
"""
Теперь давайте разберемся, как можно инициализировать модель, то есть создать экземпляр класса модели CourseSchema.
"""
    # <1> Стандартный способ = Инициализируем модель CourseSchema через передачу аргументов
print('\n1. Стандартный способ')
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week")
print(f'Course default model: {course_default_model}, type: {type(course_default_model)}')
print('='*100)

    # <2> Инициализация с использованием словаря = Инициализируем модель CourseSchema через распаковку словаря
print('\n2. Инициализация с использованием словаря')
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"}
course_dict_model = CourseSchema(**course_dict)
print(f'Course dict model: {course_dict_model}, type course_dict_model: {type(course_dict_model)}')
print('='*100)

    # <3> Инициализация с использованием JSON = Инициализируем модель CourseSchema через JSON
print('\n3. Инициализация с использованием JSON')
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print(f'Course JSON model: {course_json_model}, type course_json_model: {type(course_json_model)}')
print('='*100)

    # <3*> Если у нас есть JSON-файл, мы можем загрузить его в Pydantic-модель так:
"""
import json

with open("course.json", "r") as file:
    course_data = file.read()

course_model = CourseSchema.model_validate_json(course_data)
print(course_model)
"""





# 4.1. Обратная конвертация (из модели в JSON)
print('\nОбратная конвертация (из модели в JSON)')
print('Когда мы сериализуем Pydantic-модель обратно в JSON (dict() или json()), Pydantic по умолчанию сохраняет Python-стиль именования (snake_case).')
print(course_dict_model.model_dump())

print('Но если нам нужно вернуть JSON в camelCase, то можно использовать by_alias=True:')
print(course_dict_model.model_dump(by_alias=True))
print('='*100)

# 4.2. Использование alias_generator для автоматического преобразования
"""Если в API все поля приходят в camelCase, то вместо того, чтобы указывать alias вручную для каждого поля, можно автоматизировать процесс с помощью alias_generator:
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CourseSchema(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str


course_data = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"}

course_model = CourseSchema(**course_data)
print(course_model.model_dump(by_alias=True))
"""

"""
Что здесь происходит?

alias_generator=to_camel    автоматически превращает snake_case в camelCase.
populate_by_name=True       позволяет передавать как camelCase, так и snake_case без ошибок.
model_dump(by_alias=True)   Pydantic сам приводит имена полей в camelCase.
"""