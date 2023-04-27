from apps.users.serializers.user import UserInputSerializer, UserOutputSerializer
from apps.users.services.user import create_user, update_user_by_user

from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response


@extend_schema(request=UserInputSerializer, responses=UserOutputSerializer)
class UserCreateAndRetrieveApiView(GenericAPIView):
    def get(self, request: Request) -> Response:
        pass

    def post(self, request: Request) -> Response:
        response = create_user(data=request.data)
        return Response(response, 200)


@extend_schema(request=UserInputSerializer, responses=UserOutputSerializer)
class UserUpdateAndRetrieveApiView(GenericAPIView):
    def get(self, request: Request) -> Response:
        pass

    def put(self, request: Request, id: int) -> Response:
        response = update_user_by_user(data=request.data, id=id)
        return Response(response, 200)

    def delete(self, request: Request) -> Response:
        pass
