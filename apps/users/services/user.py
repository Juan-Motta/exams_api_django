from typing import Dict
from apps.users.serializers.user import UserSerializer

def create_user(data: Dict) -> Dict:
    serializer = UserSerializer(data=data)
    if not serializer.is_valid():
        return serializer.errors
    return serializer.data