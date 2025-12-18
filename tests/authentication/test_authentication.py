import pytest

from http import HTTPStatus

from clients.authentication.authentication_client import LoginRequestSchema, LoginResponseSchema, AuthenticationClient
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:

    def test_login(self, authentication_client: AuthenticationClient, function_user: UserFixture):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)

        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())