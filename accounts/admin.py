
from django import forms
from django.contrib import admin, messages
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.db import transaction, DatabaseError

from .models import (
    Users,
    Roles,
    Permissions,
    UserRoles,
    RolePermissions,
    Organizations,
    OrgMemberships,
    LoginSessions,
    OtpCodes,
)


# ==========================================================
# CUSTOM GROUP FORM
# Modern checkbox-based permission selection
# ==========================================================

class GroupAdminForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = "__all__"

        widgets = {
            "permissions": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "checkbox-select-multiple"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Permission field description
        self.fields["permissions"].help_text = (
            "Select the permissions you want to assign "
            "to members of this group."
        )

        # Organize permissions alphabetically by application,
        # model and permission codename.
        self.fields["permissions"].queryset = (
            Permission.objects
            .select_related("content_type")
            .order_by(
                "content_type__app_label",
                "content_type__model",
                "codename",
            )
        )


# ==========================================================
# CUSTOM USER ADMIN
# ==========================================================

class CustomUserAdmin(UserAdmin):

    def save_model(self, request, obj, form, change):

        try:
            with transaction.atomic():

                super().save_model(
                    request,
                    obj,
                    form,
                    change
                )

            action = "updated" if change else "created"

            messages.success(
                request,
                f"User '{obj.username}' was successfully "
                f"{action} and saved to the database."
            )

        except DatabaseError as e:

            messages.error(
                request,
                f"Database Error: Could not save user. "
                f"Transaction rolled back. Details: {e}"
            )

            raise

        except Exception as e:

            messages.warning(
                request,
                f"An error occurred while saving the user. "
                f"Details: {e}"
            )

            raise


# ==========================================================
# CUSTOM GROUP ADMIN
# Modern permissions management
# ==========================================================

class CustomGroupAdmin(GroupAdmin):

    form = GroupAdminForm

    # Use checkboxes instead of Django's default
    # horizontal filter interface.
    filter_horizontal = ()

    # Simplified group editing interface.
    fieldsets = (
        (
            "Group Information",
            {
                "fields": ("name",),
                "description": "Enter the group name.",
            },
        ),
        (
            "Group Permissions",
            {
                "fields": ("permissions",),
                "description": (
                    "Select the permissions that members "
                    "of this group should have."
                ),
            },
        ),
    )

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )

    def save_model(self, request, obj, form, change):

        try:
            with transaction.atomic():

                super().save_model(
                    request,
                    obj,
                    form,
                    change
                )

            action = "updated" if change else "created"

            messages.success(
                request,
                f"Group '{obj.name}' was successfully "
                f"{action} and saved to the database."
            )

        except DatabaseError as e:

            messages.error(
                request,
                f"Database Error: Could not save group. "
                f"Transaction rolled back. Details: {e}"
            )

            raise

        except Exception as e:

            messages.warning(
                request,
                f"An error occurred while saving the group. "
                f"Details: {e}"
            )

            raise


# ==========================================================
# DJANGO AUTHENTICATION MODEL REGISTRATION
# ==========================================================

# Unregister existing User admin if already registered.
try:
    admin.site.unregister(User)

except admin.sites.NotRegistered:
    pass


# Register custom User admin.
admin.site.register(
    User,
    CustomUserAdmin
)


# Unregister existing Group admin if already registered.
try:
    admin.site.unregister(Group)

except admin.sites.NotRegistered:
    pass


# Register custom Group admin.
admin.site.register(
    Group,
    CustomGroupAdmin
)


# ==========================================================
# APPLICATION MODEL REGISTRATION
# ==========================================================

application_models = [
    Users,
    Roles,
    Permissions,
    UserRoles,
    RolePermissions,
    Organizations,
    OrgMemberships,
    LoginSessions,
    OtpCodes,
]


for model in application_models:

    try:
        admin.site.register(model)

    except admin.sites.AlreadyRegistered:
        pass
