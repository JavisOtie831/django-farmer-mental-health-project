"""
Core models — generated from live DB.
"""
import uuid
from django.db import models


class AdminAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    level = models.TextField()
    name = models.TextField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code = models.TextField(unique=True, blank=True, null=True)
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
        db_table = 'afya"."admin_areas'




class CropTypes(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField(unique=True)
    name = models.TextField()
    category = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."crop_types'




class FarmActivities(models.Model):
    id = models.UUIDField(primary_key=True)
    farm = models.ForeignKey('core.Farms', models.DO_NOTHING)
    crop_type = models.ForeignKey('core.CropTypes', models.DO_NOTHING, blank=True, null=True)
    activity_type = models.TextField()
    activity_date = models.DateField()
    input_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."farm_activities'




class Farmers(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.OneToOneField('accounts.Users', models.DO_NOTHING, blank=True, null=True)
    admin_area = models.ForeignKey('core.AdminAreas', models.DO_NOTHING, blank=True, null=True)
    research_pid = models.UUIDField()
    display_name_enc = models.BinaryField(blank=True, null=True)
    national_id_enc = models.BinaryField(blank=True, null=True)
    year_of_birth = models.SmallIntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    primary_language = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."farmers'




class Farms(models.Model):
    id = models.UUIDField(primary_key=True)
    farmer = models.ForeignKey('core.Farmers', models.DO_NOTHING)
    name = models.TextField(blank=True, null=True)
    size_hectares = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    admin_area = models.ForeignKey('core.AdminAreas', models.DO_NOTHING, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
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
        db_table = 'afya"."farms'




class HarvestRecords(models.Model):
    id = models.UUIDField(primary_key=True)
    farm = models.ForeignKey('core.Farms', models.DO_NOTHING)
    crop_type = models.ForeignKey('core.CropTypes', models.DO_NOTHING, blank=True, null=True)
    harvest_date = models.DateField()
    yield_kg = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    income_kes = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
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
        db_table = 'afya"."harvest_records'


