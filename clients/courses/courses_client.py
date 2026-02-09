import allure

from httpx import Response
from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.courses.courses_schema import *
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes



class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    @allure.step("Get course by id: {course_id}")
    @tracker.track_coverage_httpx(f'{APIRoutes.COURSES}/{{course_id}}')
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.COURSES}/{course_id}")

    def get_course(self, course_id: str) -> GetCourseResponseSchema:
        response = self.get_course_api(course_id)
        return response.json()


    @allure.step("Get courses")
    @tracker.track_coverage_httpx(APIRoutes.COURSES)
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=APIRoutes.COURSES, params=query.model_dump(by_alias=True))

    def get_courses(self, query: GetCoursesQuerySchema) -> GetCoursesResponseSchema:
        response = self.get_courses_api(query)
        return GetCoursesResponseSchema.model_validate_json(response.text)


    @allure.step("Create course")
    @tracker.track_coverage_httpx(APIRoutes.COURSES)
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url=APIRoutes.COURSES, json=request.model_dump(by_alias=True))

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


    @allure.step("Update course by id: {course_id}")
    @tracker.track_coverage_httpx(f'{APIRoutes.COURSES}/{{course_id}}')
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"{APIRoutes.COURSES}/{course_id}", json=request.model_dump(by_alias=True))

    def update_course(self, course_id: str, request: UpdateCourseRequestSchema) -> UpdateCourseResponseSchema:
        response = self.update_course_api(course_id, request)
        return UpdateCourseResponseSchema.model_validate_json(response.text)


    @allure.step("Delete course by id: {course_id}")
    @tracker.track_coverage_httpx(f'{APIRoutes.COURSES}/{{course_id}}')
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")


# Добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))