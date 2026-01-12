from pydantic import BaseModel, HttpUrl, Field, FilePath
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    Attributes:
        id: str
        url: str
        filename: str
        directory: str
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    Attributes:
        filename: str
        directory: str
        upload_file: str - required
    """
    filename: str       = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str      = Field(default='tests')  # путь к директории, куда файл должен быть загружен
    upload_file: FilePath                         # путь к файлу на локальной машине, который будет загружен


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Описание структуры запроса получения файла.
    """
    file: FileSchema