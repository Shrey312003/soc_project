from rest_framework.serializers import ModelSerializer
from .models import Admin_info,Ta_info

class Admin_infoSerializer(ModelSerializer):
    class Meta:
        model =  Admin_info
        fields = '__all__'

class Ta_infoSerializer(ModelSerializer):
    class Meta:
        model =  Ta_info
        fields = '__all__'