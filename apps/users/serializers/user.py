from typing import Dict

from apps.users.models.user import User, StateChoises, ProfileChoises, CountryChoises

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
            "password",
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
    state = serializers.ChoiceField(choices=StateChoises.choices, allow_null=True)
    country = serializers.ChoiceField(choices=CountryChoises.choices, allow_null=True)
    profiles = serializers.ChoiceField(choices=ProfileChoises.choices, allow_null=True)

    @transaction.atomic
    def create(self, validated_data: Dict) -> User:
        user = User.objects.create_user(
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_email"),
            phone=validated_data.get("phone"),
            nid=validated_data.get("nid"),
            birth=validated_data.get("birth"),
            password=validated_data.get("password"),
            state=validated_data.get("state"),
            country=validated_data.get("country"),
            profile=validated_data.get("profile")
        )
        user.save()
        return user

    def update(self, instance: User, validated_data: Dict) -> User:
        return

    def to_representation(self, instance):
        return UserOutputSerializer(instance).data
