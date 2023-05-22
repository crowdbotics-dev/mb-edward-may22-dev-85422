from django.contrib import admin
from .models import Just_one_field,Model3,Model4,Model5,Model6,User
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
admin.site.register(Model3)
admin.site.register(Model4)
admin.site.register(Just_one_field)
admin.site.register(Model5)
admin.site.register(Model6)
