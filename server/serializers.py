from rest_framework.serializers import ModelSerializer

from .models import SmartFarm

class PatentAttorneyBaseModelSerializer(ModelSerializer):
    class Meta:
        model = PatentAttorney
        fields = '__all__'

class PatentAttorneyListModelSerializer(PatentAttorneyBaseModelSerializer):
    class Meta(PatentAttorneyBaseModelSerializer.Meta):
        fields = ['id', 'image', 'name', 'license_acquisition_type', 'office_address']