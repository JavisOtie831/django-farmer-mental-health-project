from django.contrib import admin
from .models import (
    AdminAreas, Farmers, CropTypes, Farms, FarmActivities, HarvestRecords,
)
for m in [AdminAreas, Farmers, CropTypes, Farms, FarmActivities, HarvestRecords]:
    admin.site.register(m)
