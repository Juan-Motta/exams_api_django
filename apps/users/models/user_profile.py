from apps.users.validators.user_profile import validate_name

from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=64, validators=[validate_name])
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users_profiles"

    def clean_name(self) -> str:
        self.name = self.name.lower().strip()

    def clean(self) -> None:
        self.clean_name()

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"<UserProfile id={self.id} name={self.name} active={self.active}>"
        )
