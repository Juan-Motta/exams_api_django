from typing import Any, Optional

from django.contrib.auth.models import BaseUserManager


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
        is_staff: bool,
        is_superuser: bool,
        **extra_fields
    ) -> Any:
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            nid=nid,
            birth=birth,
            state_id=state,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
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
        password: Optional[str] = None,
        **extra_fields
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
            is_staff=False,
            is_superuser=False,
            **extra_fields
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
        password: Optional[str] = None,
        **extra_fields
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
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
