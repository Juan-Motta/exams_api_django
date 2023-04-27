from typing import Dict

from apps.users.models.user import User
from apps.users.serializers.user import UserSerializer
from core.schemas.responses import ApiResponse, ErrorResponse

from django.core.exceptions import ValidationError


def create_user(data: Dict) -> Dict:
    serializer = UserSerializer(data=data)
    if not serializer.is_valid():
        return serializer.errors
    try:
        serializer.save()
    except ValidationError as e:
        return ErrorResponse(
            message="error at creating user", data=dict(e)
        ).to_dict()
    return ApiResponse(data=serializer.data).to_dict()


def update_user_by_user(id: int, data: Dict) -> Dict:
    user = User.objects.filter(id=id)
    if not user.exists():
        return ErrorResponse(message="user not found").to_dict()
    serializer = UserSerializer(
        user,
        data={
            "email": data.get("email"),
            "fist_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "phone": data.get("phone"),
            "nid": data.get("nid"),
            "birth": data.get("birth"),
            "country": data.get("country"),
        },
        partial=True,
    )
    if not serializer.is_valid():
        return ErrorResponse(
            message="error at updating user", data=serializer.errors
        ).to_dict()
    serializer.save()
    return ApiResponse(data=serializer.data).to_dict()
