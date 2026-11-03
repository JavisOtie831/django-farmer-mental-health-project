"""
Accounts models — generated from live DB.
"""
import uuid
from django.db import models


class LoginSessions(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('accounts.Users', models.DO_NOTHING)
    token_id = models.TextField(unique=True)
    channel = models.TextField()  # This field type is a guess.
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    device_id = models.TextField(blank=True, null=True)
    issued_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    revoked_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."login_sessions'




class OrgMemberships(models.Model):
    id = models.UUIDField(primary_key=True)
    org = models.ForeignKey('accounts.Organizations', models.DO_NOTHING)
    user = models.ForeignKey('accounts.Users', models.DO_NOTHING)
    role_in_org = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."org_memberships'
        unique_together = (('org', 'user'),)




class Organizations(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField(unique=True)
    name = models.TextField()
    org_type = models.TextField()
    county = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."organizations'




class OtpCodes(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('accounts.Users', models.DB_CASCADE)
    code_hash = models.TextField()
    purpose = models.TextField()
    channel = models.TextField()  # This field type is a guess.
    expires_at = models.DateTimeField()
    consumed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."otp_codes'




class Permissions(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."permissions'




class RolePermissions(models.Model):
    id = models.UUIDField(primary_key=True)
    role = models.ForeignKey('accounts.Roles', models.DO_NOTHING)
    permission = models.ForeignKey('accounts.Permissions', models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."role_permissions'
        unique_together = (('role', 'permission'),)




class Roles(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField(unique=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."roles'




class UserRoles(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('accounts.Users', models.DO_NOTHING)
    role = models.ForeignKey('accounts.Roles', models.DO_NOTHING)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."user_roles'
        unique_together = (('user', 'role'),)




class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    phone_hash = models.TextField(unique=True)
    phone_enc = models.BinaryField()
    email_hash = models.TextField(unique=True, blank=True, null=True)
    email_enc = models.BinaryField(blank=True, null=True)
    full_name_enc = models.BinaryField(blank=True, null=True)
    password_hash = models.TextField(blank=True, null=True)
    pin_hash = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    last_login_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.UUIDField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by = models.UUIDField(blank=True, null=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.UUIDField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'afya"."users'
