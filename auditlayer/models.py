"""
Auditlayer models — generated from live DB.
Append-only; do not write via Django unless inserting.
"""
import uuid
from django.db import models


class ApiRequestLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_time = models.DateTimeField()
    method = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    duration_ms = models.IntegerField(blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    request_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit"."api_request_logs'


class AuditLogs(models.Model):
    # NOTE: real DB PK is composite (id, event_time), required by monthly
    # partitioning. Django admin cannot register composite PKs, so we treat
    # `id` (a random UUID) as the ORM-level PK. Safe because UUID collisions
    # are effectively impossible and this model is read-only in admin.
    id = models.UUIDField(primary_key=True)
    event_seq = models.BigIntegerField(null=True, blank=True)
    event_time = models.DateTimeField()
    actor_id = models.UUIDField(blank=True, null=True)
    actor_role = models.TextField(blank=True, null=True)
    action = models.TextField()
    table_schema = models.TextField(blank=True, null=True)
    table_name = models.TextField(blank=True, null=True)
    record_id = models.UUIDField(blank=True, null=True)
    old_values = models.JSONField(blank=True, null=True)
    new_values = models.JSONField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    device_id = models.TextField(blank=True, null=True)
    session_id = models.TextField(blank=True, null=True)
    request_id = models.TextField(blank=True, null=True)
    channel = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    prev_hash = models.TextField(blank=True, null=True)
    row_hash = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit"."audit_logs'
        ordering = ['-event_time']


class ConsentHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    consent_id = models.UUIDField()
    old_status = models.TextField(blank=True, null=True)
    new_status = models.TextField()
    changed_by = models.UUIDField(blank=True, null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit"."consent_history'


class DataAccessLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_time = models.DateTimeField()
    user_id = models.UUIDField(blank=True, null=True)
    dataset_id = models.UUIDField(blank=True, null=True)
    project_id = models.UUIDField(blank=True, null=True)
    variables = models.JSONField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    request_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit"."data_access_logs'


class LoginAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    attempted_at = models.DateTimeField()
    identifier = models.TextField(blank=True, null=True)
    channel = models.TextField(blank=True, null=True)
    success = models.BooleanField()
    reason = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    request_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit"."login_attempts'


class RecordHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_schema = models.TextField()
    table_name = models.TextField()
    record_id = models.UUIDField()
    changed_at = models.DateTimeField()
    changed_by = models.UUIDField(blank=True, null=True)
    old_values = models.JSONField(blank=True, null=True)
    new_values = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit"."record_history'


class SecurityEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_time = models.DateTimeField()
    event_type = models.TextField()
    severity = models.TextField()
    actor_id = models.UUIDField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    payload = models.JSONField(blank=True, null=True)
    request_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit"."security_events'