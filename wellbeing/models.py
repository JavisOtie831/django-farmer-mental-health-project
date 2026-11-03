"""
Wellbeing models — generated from live DB.
"""
import uuid
from django.db import models


class AnalysisRules(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField(unique=True)
    description = models.TextField()
    condition_sql = models.TextField()
    action = models.TextField()
    severity = models.TextField()  # This field type is a guess.
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
        db_table = 'afya"."analysis_rules'




class CheckinAssessments(models.Model):
    id = models.UUIDField(primary_key=True)
    checkin = models.OneToOneField('wellbeing.Checkins', models.DB_CASCADE)
    total_score = models.DecimalField(max_digits=6, decimal_places=2)
    risk_level = models.TextField()  # This field type is a guess.
    primary_stressor = models.TextField(blank=True, null=True)
    auto_referral = models.BooleanField()
    recommendation = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."checkin_assessments'




class CheckinResponses(models.Model):
    id = models.UUIDField(primary_key=True)
    checkin = models.ForeignKey('wellbeing.Checkins', models.DB_CASCADE)
    question = models.ForeignKey('wellbeing.Questions', models.DO_NOTHING)
    option = models.ForeignKey('wellbeing.QuestionOptions', models.DO_NOTHING, blank=True, null=True)
    raw_value = models.TextField(blank=True, null=True)
    numeric_score = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    answered_at = models.DateTimeField()
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
        db_table = 'afya"."checkin_responses'
        unique_together = (('checkin', 'question'),)




class Checkins(models.Model):
    id = models.UUIDField(primary_key=True)
    farmer = models.ForeignKey('core.Farmers', models.DO_NOTHING)
    questionnaire_version = models.ForeignKey('wellbeing.QuestionnaireVersions', models.DO_NOTHING)
    channel = models.TextField()  # This field type is a guess.
    checkin_at = models.DateTimeField()
    total_score = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    risk_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    assessment = models.ForeignKey('wellbeing.CheckinAssessments', models.DO_NOTHING, blank=True, null=True)
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
        db_table = 'afya"."checkins'




class DimensionScores(models.Model):
    id = models.UUIDField(primary_key=True)
    checkin = models.ForeignKey('wellbeing.Checkins', models.DB_CASCADE)
    dimension = models.TextField()  # This field type is a guess.
    raw_score = models.DecimalField(max_digits=6, decimal_places=2)
    normalized_score = models.DecimalField(max_digits=6, decimal_places=2)
    risk_level = models.TextField()  # This field type is a guess.
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
        db_table = 'afya"."dimension_scores'
        unique_together = (('checkin', 'dimension'),)




class QuestionOptions(models.Model):
    id = models.UUIDField(primary_key=True)
    question = models.ForeignKey('wellbeing.Questions', models.DB_CASCADE)
    option_value = models.TextField()
    label = models.TextField()
    numeric_score = models.DecimalField(max_digits=6, decimal_places=2)
    position = models.SmallIntegerField()
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
        db_table = 'afya"."question_options'
        unique_together = (('question', 'option_value'),)




class QuestionnaireVersions(models.Model):
    id = models.UUIDField(primary_key=True)
    questionnaire = models.ForeignKey('wellbeing.Questionnaires', models.DO_NOTHING)
    version_no = models.IntegerField()
    is_current = models.BooleanField()
    published_at = models.DateTimeField(blank=True, null=True)
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
        db_table = 'afya"."questionnaire_versions'
        unique_together = (('questionnaire', 'version_no'),)




class Questionnaires(models.Model):
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
        db_table = 'afya"."questionnaires'




class Questions(models.Model):
    id = models.UUIDField(primary_key=True)
    questionnaire_version = models.ForeignKey('wellbeing.QuestionnaireVersions', models.DB_CASCADE)
    code = models.TextField()
    position = models.SmallIntegerField()
    text = models.TextField()
    qtype = models.TextField()  # This field type is a guess.
    dimension = models.TextField()  # This field type is a guess.
    is_reverse = models.BooleanField()
    weight = models.DecimalField(max_digits=5, decimal_places=4)
    max_raw_score = models.DecimalField(max_digits=6, decimal_places=2)
    is_required = models.BooleanField()
    is_active = models.BooleanField()
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
        db_table = 'afya"."questions'
        unique_together = (('questionnaire_version', 'code'), ('questionnaire_version', 'position'),)




class ScoringRules(models.Model):
    id = models.UUIDField(primary_key=True)
    questionnaire_version = models.ForeignKey('wellbeing.QuestionnaireVersions', models.DB_CASCADE)
    scope = models.TextField()
    dimension = models.TextField(blank=True, null=True)  # This field type is a guess.
    min_score = models.DecimalField(max_digits=6, decimal_places=2)
    max_score = models.DecimalField(max_digits=6, decimal_places=2)
    risk_level = models.TextField()  # This field type is a guess.
    advice_text = models.TextField(blank=True, null=True)
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
        db_table = 'afya"."scoring_rules'




class StressorLogs(models.Model):
    id = models.UUIDField(primary_key=True)
    farmer = models.ForeignKey('core.Farmers', models.DO_NOTHING)
    stressor_type = models.ForeignKey('wellbeing.StressorTypes', models.DO_NOTHING)
    checkin = models.ForeignKey('wellbeing.Checkins', models.DO_NOTHING, blank=True, null=True)
    severity = models.SmallIntegerField(blank=True, null=True)
    logged_at = models.DateTimeField()
    notes_enc = models.BinaryField(blank=True, null=True)
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
        db_table = 'afya"."stressor_logs'




class StressorTypes(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField(unique=True)
    name = models.TextField()
    dimension = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'afya"."stressor_types'


