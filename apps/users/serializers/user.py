from typing import Dict
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.users.models.user import User
from django.db import transaction

class UserInputSerializer(serializers.ModelSerializer):
    country = serializers.IntegerField()
    
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone", "nid", "birth", "password", "country")
        
class UserOutputSerializer(serializers.ModelSerializer):
    state = serializers.IntegerField()
    country = serializers.IntegerField()
    profiles = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )
    
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone", "nid", "birth", "password", "state", "country", "profiles")


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    nid = serializers.CharField()
    birth = serializers.CharField()
    password = serializers.CharField()
    state = serializers.IntegerField()
    country = serializers.IntegerField()
    profiles = serializers.ListField(
        child=serializers.IntegerField(min_value=1)
    )

    @transaction.atomic
    def create(self, validated_data: Dict) -> User:
        user = User.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_email"],
            phone=validated_data["phone"],
            nid=validated_data["nid"],
            birth=validated_data["birth"],
            password=validated_data["password"],
            state_id=validated_data["state"],
            country_id=validated_data["country"]
        )
        for profile in validated_data["profiles"]:
            user.profiles.add(profile)
        user.save()
        return user
    
    def update(self, instance: User, validated_data: Dict) -> User:
        return
    
    def to_representation(self, instance):
        return UserOutputSerializer(instance).data