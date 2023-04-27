from typing import Dict

from apps.users.constants import ProfileConstants, StateConstants
from apps.users.models.user import CountryChoises, ProfileChoises, StateChoises, User

from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "nid",
            "birth",
            "password",
            "country",
        )


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "nid",
            "birth",
            "state",
            "country",
            "profile",
        )


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField(allow_null=True)
    nid = serializers.CharField(allow_null=True)
    birth = serializers.CharField(allow_null=True)
    password = serializers.CharField()
    state = serializers.ChoiceField(
        choices=StateChoises.choices, required=False
    )
    country = serializers.ChoiceField(
        choices=CountryChoises.choices, allow_null=True
    )
    profiles = serializers.ChoiceField(
        choices=ProfileChoises.choices, required=False
    )
    password = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)

    @transaction.atomic
    def create(self, data: Dict) -> User:
        user = User.objects.create_user(
            email=data.get("email"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone=data.get("phone"),
            nid=data.get("nid"),
            birth=data.get("birth"),
            password=data.get("password"),
            country=data.get("country"),
        )
        return user

    def update(self, instance: User, data: Dict) -> User:
        for key, value in data.items():
            setattr(instance, key, value)
        self._set_password(instance=instance, data=data)

    def _set_password(self, instance: User, data: Dict) -> str:
        if "password" in data:
            instance.set_password(data["password"])
        else:
            return

    def to_representation(self, instance):
        return UserOutputSerializer(instance).data
