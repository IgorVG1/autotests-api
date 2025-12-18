from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from tools.fakers import fake



class FileSchema(BaseModel):
    """
    Attributes:
        id: str
        filename: str
        directory: str
        url: str
    """

    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    """
    Attributes:
        id: str
        email: str
        last_name: str (lastName)
        first_name: str (firstName)
        middle_name: str (middleName)
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    last_name: str      = Field(alias='lastName')
    first_name: str     = Field(alias='firstName')
    middle_name: str    = Field(alias='middleName')


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    Attributes:
        id: str
        title: str
        max_score: int (maxScore)
        min_score: int (minScore)
        description: str
        estimated_time: str (estimatedTime)
        preview_file: FileSchema (previewFile)
        created_by_user: UserSchema (createdByUser)
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int              = Field(alias='maxScore')
    min_score: int              = Field(alias="minScore")
    description: str
    preview_file: FileSchema    = Field(alias='previewFile')
    estimated_time: str         = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    Attributes:
        user_id: str
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    Attributes:
        title: str
        max_score: int (maxScore)
        min_score: int (minScore)
        description: str
        estimated_time: str (estimatedTime)
        preview_file_id: FileSchema (previewFileId)
        created_by_user_id: UserSchema (createdByUserId)
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str              = Field(default_factory=fake.sentence)
    max_score: int          = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int          = Field(alias='minScore', default_factory=fake.min_score)
    description: str        = Field(default_factory=fake.text)
    estimated_time: str     = Field(alias='estimatedTime', default_factory=fake.estimated_time)
    # Для негативных тестов (например, "Файл не найден", "Пользователь не найден") можно использовать случайные UUID
    preview_file_id: str    = Field(alias='previewFileId', default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias='createdByUserId', default_factory=fake.uuid4)


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    Attributes:
        title: str
        max_score: int (maxScore)
        min_score: int (minScore)
        description: str
        estimated_time: str (estimatedTime)
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None          = Field(default_factory=fake.sentence)
    max_score: int | None      = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None      = Field(alias='minScore', default_factory=fake.min_score)
    description: str | None    = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class GetCourseResponseSchema(BaseModel):
    course: CourseSchema


class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]


class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema