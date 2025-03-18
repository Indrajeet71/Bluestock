from rest_framework import serializers
from .models import IPOCompany

class IPOCompanySerializer(serializers.ModelSerializer):
    listing_gain = serializers.SerializerMethodField()
    current_return = serializers.SerializerMethodField()

    class Meta:
        model = IPOCompany
        fields = '__all__'

    def get_listing_gain(self, obj):
        return obj.listing_gain

    def get_current_return(self, obj):
        return obj.current_return

    def validate(self, data):
        if 'close_date' in data and 'open_date' in data:
            if data['close_date'] < data['open_date']:
                raise serializers.ValidationError("Close date cannot be before open date.")
        if 'listing_price' in data and 'issue_price' in data:
            if data['listing_price'] < 0 or data['issue_price'] < 0:
                raise serializers.ValidationError("Prices must be non-negative.")
        return data
