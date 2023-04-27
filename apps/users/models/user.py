from typing import Any, Optional

from apps.users.validators import *

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.constants import ProfileConstants, StateConstants, CountryConstants


class StateChoises(models.TextChoices):
    ACTIVE = StateConstants.ACTIVE, _(StateConstants.ACTIVE)
    INACTIVE = StateConstants.INACTIVE, _(StateConstants.INACTIVE)
    PENDING = StateConstants.PENDING, _(StateConstants.PENDING)

class ProfileChoises(models.TextChoices):
    ADMINISTRATOR = ProfileConstants.ADMINISTRATOR, _(ProfileConstants.ADMINISTRATOR)
    COORDINATOR = ProfileConstants.COORDINATOR, _(ProfileConstants.COORDINATOR)
    STUDENT = ProfileConstants.STUDENT, _(ProfileConstants.STUDENT)
    SUPPORT = ProfileConstants.SUPPORT, _(ProfileConstants.SUPPORT)
    TEACHER = ProfileConstants.TEACHER, _(ProfileConstants.TEACHER)
    USER = ProfileConstants.USER, _(ProfileConstants.USER)

class CountryChoises(models.TextChoices):
    COL = CountryConstants.COL, _(CountryConstants.COL)
    ECU = CountryConstants.ECU, _(CountryConstants.ECU)
    ESP = CountryConstants.ESP, _(CountryConstants.ESP)
    MEX = CountryConstants.MEX, _(CountryConstants.MEX)
    PER = CountryConstants.PER, _(CountryConstants.PER)

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
        country: str,
        state: str,
        profile: str,
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
            country=country,
            state=state,
            profile=profile,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )
        user.set_password(password)
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
            state=StateConstants.PENDING,
            profile=ProfileConstants.USER,
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
        country: str,
        password: Optional[str] = None,
        **extra_fields,
    ) -> Any:
        print(StateConstants.ACTIVE)
        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            nid=nid,
            birth=birth,
            password=password,
            state=StateConstants.ACTIVE,
            profile=ProfileConstants.ADMINISTRATOR,
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
    nid = models.CharField(
        max_length=16, null=True, blank=True, validators=[validate_nid]
    )
    birth = models.DateField(
        null=True, blank=True, validators=[validate_birth]
    )
    password = models.CharField(max_length=128)

    state = models.CharField(
        max_length=16,
        choices=StateChoises.choices,
        default=StateChoises.PENDING
    )
    profile = models.CharField(
        max_length=16,
        choices=ProfileChoises.choices,
        default=ProfileChoises.USER
    )
    country = models.CharField(
        max_length=32,
        choices=CountryChoises.choices,
    )

    is_active = models.BooleanField(default=True)
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

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"<User id={self.id} email={self.email} is_active={self.active}>"
