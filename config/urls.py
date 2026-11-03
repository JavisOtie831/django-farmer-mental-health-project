from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout_immediately(request):
    auth_logout(request)
    return redirect('/admin/login/?next=/admin/')

urlpatterns = [
    path('admin/logout/', logout_immediately, name='logout_immediately'),
    path('admin/', admin.site.urls),
    # THIS LINE REGISTERS THE 'accounts' NAMESPACE:
    path('accounts/', include('accounts.urls')),
]