from django.shortcuts import render
from .serializers import UserSRL, Login_Serializer, ChangePasswordSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema


class RegstrView(APIView):
    queryset = User.objects.all()
    serializer_class = User

    @swagger_auto_schema(request_body=UserSRL)
    def post(self, request):
        phone = request.data.get("phone")
        serializer = UserSRL(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(phone=phone).first()
        return Response(serializer.errors)


class Login(APIView):
    queryset = User.objects.all()
    serializer_cl = Login_Serializer

    @swagger_auto_schema(request_body=Login_Serializer)
    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        user = User.objects.all().filter(name=name, password=password)
        return Response({"Message": "Succes"})


class UpdateuserPassword(APIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def patch(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        corfim_password = request.data.get("corfim_password")
        tekshirish_email = User.objects.all().filter(email=email)
        if tekshirish_email:
            if password == corfim_password:
                update = User.objects.all().filter(email=email).update(password=corfim_password)
                return Response({"msg": "password is changed"})
            else:
                return Response({"msg": "password != password_corfim"})
        else:
            return Response({"msg": "email not found"})
