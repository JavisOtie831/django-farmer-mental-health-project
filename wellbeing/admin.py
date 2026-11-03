from django.contrib import admin
from .models import (
    Questionnaires, QuestionnaireVersions, Questions, QuestionOptions,
    Checkins, CheckinResponses, StressorTypes, StressorLogs,
    ScoringRules, DimensionScores, CheckinAssessments, AnalysisRules,
)
for m in [Questionnaires, QuestionnaireVersions, Questions, QuestionOptions,
          Checkins, CheckinResponses, StressorTypes, StressorLogs,
          ScoringRules, DimensionScores, CheckinAssessments, AnalysisRules]:
    admin.site.register(m)
