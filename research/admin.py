from django.contrib import admin
from .models import (
    Institutions, ResearchProjects, ProjectMembers, EthicsApprovals,
    Consents, DataAccessRequests, Datasets, DatasetExports, ResearchPidMap,
)
for m in [Institutions, ResearchProjects, ProjectMembers, EthicsApprovals,
          Consents, DataAccessRequests, Datasets, DatasetExports, ResearchPidMap]:
    admin.site.register(m)
