from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .models import Profile
from .models import UserActivity


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    model = User

    list_display = (
        'email',
        'productivity_score',
        'daily_budget_limit',
        'focus_mode',
        'is_staff',
    )

    ordering = ('email',)

    fieldsets = (

        (None, {
            'fields': (
                'email',
                'password',
            )
        }),

        ('Personal Info', {
            'fields': (
                'productivity_score',
                'daily_budget_limit',
                'focus_mode',
            )
        }),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),

        ('Important Dates', {
            'fields': (
                'last_login',
            )
        }),
    )

    add_fieldsets = (

        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    search_fields = ('email',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'preferred_currency',
        'timezone',
    )


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'event_type',
        'timestamp',
    )