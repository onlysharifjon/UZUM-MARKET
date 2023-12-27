from django.shortcuts import render
from .serializers import UserSRL, Login_Serializer
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema



class RegstrView(APIView):
    queryset = User.objects.all()
    serializer_class = User
    @swagger_auto_schema(request_body = UserSRL)
    def post(self, request):
        phone = request.data.get("phone")
        serializer = UserSRL(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(phone = phone).first()
        return Response(serializer.errors)

class Login(APIView):
    queryset = User.objects.all()
    serializer_cl = Login_Serializer
    @swagger_auto_schema(request_body=Login_Serializer)
    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        user = User.objects.all().filter(name=name, password=password)
        return Response({"Message":"Succes"})


