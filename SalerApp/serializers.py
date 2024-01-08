from rest_framework import serializers
from .models import SalerRegister


class ForLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalerRegister
        fields = '__all__'


class ForRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalerRegister
        fields = ('username', 'password')
