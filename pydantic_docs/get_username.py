from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str      = Field(alias='lastName')
    first_name: str     = Field(alias='firstName')
    middle_name: str    = Field(alias="middleName")

    def get_username(self) -> str:
        return f'{self.first_name} {self.last_name}'



# Инициализируем FileSchema c некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses")
except ValidationError as error:
    print(error)
    print(error.errors())