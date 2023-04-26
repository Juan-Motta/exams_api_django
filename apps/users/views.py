from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from apps.users.services.user import create_user
from drf_spectacular.utils import extend_schema
from apps.users.serializers.user import UserInputSerializer, UserOutputSerializer

@extend_schema(
    request=UserInputSerializer,
    responses=UserOutputSerializer
)
class UserCreateAndRetrieveApiView(GenericAPIView):
    def get(self, request: Request) -> Response:
        pass
    
    def post(self, request: Request) -> Response:
        return Response(create_user(request.data), 200)
    

class UserUpdateAndRetrieveApiView(GenericAPIView):
    def get(self, request: Request) -> Response:
        pass
    
    def put(self, request: Request) -> Response:
        pass
    
    def delete(self, request: Request) -> Response:
        pass