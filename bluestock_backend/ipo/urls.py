from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IPOCompanyViewSet

router = DefaultRouter()
router.register(r'companies', IPOCompanyViewSet, basename='ipocompany')

urlpatterns = [
    path('', include(router.urls)),
]
