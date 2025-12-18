import uuid
from pydantic import BaseModel, Field





class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: str


class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str      = Field(alias='lastName')
    first_name: str     = Field(alias='firstName')
    middle_name: str    = Field(alias='middleName')


class CourseSchema(BaseModel):
    id: str                     = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    max_score: int              = Field(alias='maxScore')
    min_score: int              = Field(alias="minScore")
    description: str
    preview_file: FileSchema    = Field(alias='previewFile')
    estimated_time: str         = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')





""" 1. Инициализация через аргументы. """
# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchema( id="file-id",
                            url="http://localhost:8000",
                            filename="file.png",
                            directory="courses" ),
    estimatedTime="1 week",
    createdByUser=UserSchema(   id="user-id",
                                email="user@gmail.com",
                                lastName="Bond",
                                firstName="Zara",
                                middleName="Alise" ))
print(f'Course default model: {course_default_model}')



""" 2. Инициализация через dict (распаковка словаря). """
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
                        "id": "file-id",
                        "url": "http://localhost:8000",
                        "filename": "file.png",
                        "directory": "courses"
                   },
    "estimatedTime": "1 week",
    "createdByUser": {
                        "id": "user-id",
                        "email": "user@gmail.com",
                        "lastName": "Bond",
                        "firstName": "Zara",
                        "middleName": "Alise"
                     }}
course_dict_model = CourseSchema(**course_dict)
print(f'Course dict model: {course_dict_model}')



""" 3. Инициализация через JSON: """
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
                    "id": "file-id",
                    "url": "http://localhost:8000",
                    "filename": "file.png",
                    "directory": "courses"
                    },
    "estimatedTime": "1 week",
    "createdByUser": {
                        "id": "user-id",
                        "email": "user@gmail.com",
                        "lastName": "Bond",
                        "firstName": "Zara",
                        "middleName": "Alise"
                      }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print(f'Course JSON model: {course_json_model}')