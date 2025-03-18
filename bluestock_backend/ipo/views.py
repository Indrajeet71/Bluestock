from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import IPOCompany
from .serializers import IPOCompanySerializer

class IPOCompanyViewSet(viewsets.ModelViewSet):
    queryset = IPOCompany.objects.all().order_by('-listing_date')
    serializer_class = IPOCompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, modify for logged-in users

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['symbol', 'issue_type', 'open_date', 'close_date']
    search_fields = ['name', 'symbol']
    ordering_fields = ['issue_price', 'listing_date', 'market_price']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]  # Only admins can modify IPO data
        return super().get_permissions()
