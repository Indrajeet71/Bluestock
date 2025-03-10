from rest_framework import serializers
from .models import IPOCompany

class IPOCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = IPOCompany
        fields = '__all__'
