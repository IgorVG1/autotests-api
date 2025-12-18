import pytest
from pydantic import BaseModel

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseResponseSchema, CreateCourseRequestSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

    @property
    def id(self) -> str:
        return self.response.course.id

@pytest.fixture()
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture()
def function_course(courses_client: CoursesClient, function_user: UserFixture, function_file: FileFixture) -> CourseFixture:
    request = CreateCourseRequestSchema(previewFileId=function_file.id, createdByUserId=function_user.id)
    response = courses_client.create_course(request=request)
    return CourseFixture(request=request, response=response)