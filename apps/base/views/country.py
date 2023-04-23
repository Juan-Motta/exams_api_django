from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response


class CountryAPIView(GenericAPIView):
    def get(self, request: Request) -> Response:
        return Response({"message": "Hola"})
