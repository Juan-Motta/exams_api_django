from apps.users.validators import validate_name

from django.db import models


class UserState(models.Model):
    name = models.CharField(max_length=64, validators=[validate_name])
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users_states"

    def clean_name(self) -> str:
        self.email = self.email.lower().strip()

    def clean(self) -> None:
        self.clean_name()

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"<UserState id={self.id} name={self.name} active={self.active}>"
        )
