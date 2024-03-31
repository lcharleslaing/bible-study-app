from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin


# Define a new User admin
class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    # You can customize the admin list view, forms, etc., as needed here
    pass


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
