from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('email', 'national_id', 'city', 'bio',
                                                                  'experience_level', 'programming_languages')}), )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
