"""
Research models — generated from live DB.
"""
import uuid
from django.db import models


class Consents(models.Model):
    id = models.UUIDField(primary_key=True)
    project = models.ForeignKey('research.ResearchProjects', models.DB_CASCADE)
    farmer = models.ForeignKey('core.Farmers', models.DO_NOTHING)
    status = models.TextField()  # This field type is a guess.
    granted_at = models.DateTimeField(blank=True, null=True)
    withdrawn_at = models.DateTimeField(blank=True, null=True)
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
        db_table = 'afya"."consents'
        unique_together = (('project', 'farmer'),)




class DataAccessRequests(models.Model):
    id = models.UUIDField(primary_key=True)
    project = models.ForeignKey('research.ResearchProjects', models.DO_NOTHING)
    requested_by = models.ForeignKey('accounts.Users', models.DO_NOTHING, db_column='requested_by')
    variables = models.JSONField()
    justification = models.TextField()
    status = models.TextField()
    reviewed_at = models.DateTimeField(blank=True, null=True)
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
        db_table = 'afya"."data_access_requests'




class DatasetExports(models.Model):
    id = models.UUIDField(primary_key=True)
    dataset = models.ForeignKey('research.Datasets', models.DO_NOTHING)
    user = models.ForeignKey('accounts.Users', models.DO_NOTHING)
    exported_at = models.DateTimeField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
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
        db_table = 'afya"."dataset_exports'




class Datasets(models.Model):
    id = models.UUIDField(primary_key=True)
    request = models.ForeignKey('research.DataAccessRequests', models.DO_NOTHING)
    row_count = models.IntegerField()
    k_anonymity_level = models.SmallIntegerField()
    checksum = models.TextField()
    file_url = models.TextField()
    expires_at = models.DateTimeField()
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
        db_table = 'afya"."datasets'




class EthicsApprovals(models.Model):
    id = models.UUIDField(primary_key=True)
    project = models.ForeignKey('research.ResearchProjects', models.DB_CASCADE)
    nacosti_ref = models.TextField()
    irb_ref = models.TextField(blank=True, null=True)
    issued_at = models.DateField()
    expires_at = models.DateField()
    document_url = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."ethics_approvals'




class Institutions(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    country = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."institutions'




class ProjectMembers(models.Model):
    id = models.UUIDField(primary_key=True)
    project = models.ForeignKey('research.ResearchProjects', models.DB_CASCADE)
    user = models.ForeignKey('accounts.Users', models.DO_NOTHING)
    role = models.TextField()
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
        db_table = 'afya"."project_members'
        unique_together = (('project', 'user'),)




class ResearchProjects(models.Model):
    id = models.UUIDField(primary_key=True)
    institution = models.ForeignKey('research.Institutions', models.DO_NOTHING)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."research_projects'




class ResearchPidMap(models.Model):
    research_pid = models.UUIDField(primary_key=True)
    farmer_id = models.UUIDField(unique=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'research"."research_pid_map'
