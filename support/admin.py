from django.contrib import admin
from .models import (
    Counselors, Referrals, PeerGroups, GroupMembers,
    Subscriptions, Payments, Notifications,
)
for m in [Counselors, Referrals, PeerGroups, GroupMembers,
          Subscriptions, Payments, Notifications]:
    admin.site.register(m)
