from rest_framework import serializers
from .models import User
class UserSRL(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class Login_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"