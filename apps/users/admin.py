from apps.users.models.user import User
from apps.users.models.user_profile import UserProfile
from apps.users.models.user_state import UserState

from django.contrib import admin

admin.site.register([User, UserState, UserProfile])
