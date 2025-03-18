from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ipo/', include('ipo.urls')),  # Ensure 'ipo' app has urls.py configured
    path('', lambda request: HttpResponseRedirect('/ipo/')),  # Redirect root to /ipo/
]
