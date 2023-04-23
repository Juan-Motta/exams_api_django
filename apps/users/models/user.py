from apps.base.models.country import Country
from apps.users.managers.user import UserManager
from apps.users.models.user_profile import UserProfile
from apps.users.models.user_state import UserState
from apps.users.validators.user import *

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=128, unique=True)
    first_name = models.CharField(
        max_length=128, validators=[validate_first_name]
    )
    last_name = models.CharField(
        max_length=128, validators=[validate_last_name]
    )
    phone = models.CharField(
        max_length=16, null=True, validators=[validate_phone]
    )
    nid = models.CharField(max_length=16, null=True, validators=[validate_nid])
    birth = models.DateField(null=True, validators=[validate_birth])
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
    ]

    def clean_email(self) -> str:
        self.email = self.email.lower().strip()

    def clean_first_name(self) -> str:
        self.first_name = self.first_name.lower().strip()

    def clean_last_name(self) -> str:
        self.last_name = self.last_name.lower().strip()

    def clean_phone(self) -> str:
        self.phone = self.phone.lower().strip()

    def clean_nid(self) -> str:
        self.nid = self.nid.lower().strip()

    def clean(self) -> None:
        self.clean_email()
        self.clean_first_name()
        self.clean_last_name()
        self.clean_phone()
        self.clean_nid()

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"<User id={self.id} email={self.email} active={self.active}>"
