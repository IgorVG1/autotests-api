import uuid
from pydantic import BaseModel, Field


"""Использование default_factory для динамических значений

Иногда значения по умолчанию должны быть уникальными или вычисляться в момент создания объекта.
Для этого используется default_factory.

Пример: генерация случайного id для курса."""
class CourseSchema(BaseModel):
    id: str             = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str          = "Python"
    max_score: int      = Field(alias='maxScore', default=100)
    min_score: int      = Field(alias='minScore', default=10)
    description: str    = "Python course"
    estimated_time: str = Field(alias='estimatedTime', default="2 weeks")

# Создадим несколько объектов модели
course1 = CourseSchema()
course2 = CourseSchema()

print(course1.id)
print(course2.id)