from typing import Any, Optional

from apps.users.models.country import Country
from apps.users.models.user_profile import UserProfile
from apps.users.models.user_state import UserState
from apps.users.validators import *

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(
        self,
        email: str,
        first_name: str,
        last_name: str,
        phone: str,
        nid: str,
        birth: str,
        password: str,
        state: int,
        profile: int,
        country: int,
        is_staff: bool,
        is_superuser: bool,
        **extra_fields,
    ) -> Any:
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            nid=nid,
            birth=birth,
            state_id=state,
            country_id=country,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self.db)
        user.profile.add(profile)
        user.save(using=self.db)
        return user

    def create_user(
        self,
        email: str,
        first_name: str,
        last_name: str,
        phone: str,
        nid: str,
        birth: str,
        state: int,
        profile: int,
        country: int,
        password: Optional[str] = None,
        **extra_fields,
    ) -> Any:
        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            nid=nid,
            birth=birth,
            password=password,
            state=state,
            profile=profile,
            country=country,
            is_staff=False,
            is_superuser=False,
            **extra_fields,
        )

    def create_superuser(
        self,
        email: str,
        first_name: str,
        last_name: str,
        phone: str,
        nid: str,
        birth: str,
        state: int,
        profile: int,
        country: int,
        password: Optional[str] = None,
        **extra_fields,
    ) -> Any:
        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            nid=nid,
            birth=birth,
            password=password,
            state=state,
            profile=profile,
            country=country,
            is_staff=True,
            is_superuser=True,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=128, unique=True)
    first_name = models.CharField(
        max_length=128, validators=[validate_first_name]
    )
    last_name = models.CharField(
        max_length=128, validators=[validate_last_name]
    )
    phone = models.CharField(
        max_length=16, null=True, blank=True, validators=[validate_phone]
    )
    nid = models.CharField(max_length=16, null=True, blank=True, validators=[validate_nid])
    birth = models.DateField(null=True, blank=True, validators=[validate_birth])
    password = models.CharField(max_length=128)

    state = models.ForeignKey(
        UserState, on_delete=models.CASCADE, related_name="users"
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="users"
    )
    profile = models.ManyToManyField(UserProfile, related_name="users")

    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        db_table = "users"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone",
        "nid",
        "birth",
        "state",
        "profile",
        "country",
    ]

    def clean_email(self) -> str:
        self.email = self.email.lower().strip()

    def clean_first_name(self) -> str:
        self.first_name = self.first_name.lower().strip()

    def clean_last_name(self) -> str:
        self.last_name = self.last_name.lower().strip()

    def clean_phone(self) -> str:
        if self.phone is not None:
            self.phone = self.phone.lower().strip()

    def clean_nid(self) -> str:
        if self.nid is not None:
            self.nid = self.nid.lower().strip()

    def clean(self) -> None:
        self.clean_email()
        self.clean_first_name()
        self.clean_last_name()
        self.clean_phone()
        self.clean_nid()
        self.clean_state()

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"<User id={self.id} email={self.email} active={self.active}>"
