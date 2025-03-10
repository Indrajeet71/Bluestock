from rest_framework import viewsets
from .models import IPOCompany
from .serializers import IPOCompanySerializer

class IPOCompanyViewSet(viewsets.ModelViewSet):
    queryset = IPOCompany.objects.all()
    serializer_class = IPOCompanySerializer
