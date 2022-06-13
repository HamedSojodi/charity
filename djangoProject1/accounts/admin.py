from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from accounts.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_editable = ('is_staff', 'is_active')
    readonly_fields = ('last_login',)
    list_filter = ('gender', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        ('', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender', 'age')}),
        ('Contact info',
         {'fields': ('phone', 'address')}),
        ('Permissions',
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates',
         {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    # )


admin.site.register(User, UserAdmin)
