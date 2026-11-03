"""
Support models — generated from live DB.
"""
import uuid
from django.db import models


class Counselors(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.OneToOneField('accounts.Users', models.DO_NOTHING, blank=True, null=True)
    org = models.ForeignKey('accounts.Organizations', models.DO_NOTHING, blank=True, null=True)
    specialty = models.TextField(blank=True, null=True)
    is_available = models.BooleanField()
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
        db_table = 'afya"."counselors'




class GroupMembers(models.Model):
    id = models.UUIDField(primary_key=True)
    peer_group = models.ForeignKey('support.PeerGroups', models.DB_CASCADE)
    farmer = models.ForeignKey('core.Farmers', models.DB_CASCADE)
    joined_at = models.DateTimeField()
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
        db_table = 'afya"."group_members'
        unique_together = (('peer_group', 'farmer'),)




class Notifications(models.Model):
    id = models.UUIDField(primary_key=True)
    farmer = models.ForeignKey('core.Farmers', models.DO_NOTHING, blank=True, null=True)
    channel = models.TextField()  # This field type is a guess.
    template = models.TextField()
    payload = models.JSONField()
    sent_at = models.DateTimeField(blank=True, null=True)
    status = models.TextField()
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
        db_table = 'afya"."notifications'




class Payments(models.Model):
    id = models.UUIDField(primary_key=True)
    subscription = models.ForeignKey('support.Subscriptions', models.DO_NOTHING, blank=True, null=True)
    amount_kes = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.TextField()
    external_ref = models.TextField(unique=True, blank=True, null=True)
    status = models.TextField()
    paid_at = models.DateTimeField(blank=True, null=True)
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
        db_table = 'afya"."payments'




class PeerGroups(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    admin_area = models.ForeignKey('core.AdminAreas', models.DO_NOTHING, blank=True, null=True)
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
        db_table = 'afya"."peer_groups'




class Referrals(models.Model):
    id = models.UUIDField(primary_key=True)
    farmer = models.ForeignKey('core.Farmers', models.DO_NOTHING)
    checkin = models.ForeignKey('wellbeing.Checkins', models.DO_NOTHING, blank=True, null=True)
    counselor = models.ForeignKey('support.Counselors', models.DO_NOTHING, blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    reason = models.TextField(blank=True, null=True)
    opened_at = models.DateTimeField()
    closed_at = models.DateTimeField(blank=True, null=True)
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
        db_table = 'afya"."referrals'




class Subscriptions(models.Model):
    id = models.UUIDField(primary_key=True)
    farmer = models.ForeignKey('core.Farmers', models.DO_NOTHING)
    plan_code = models.TextField()
    status = models.TextField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)
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
        db_table = 'afya"."subscriptions'


