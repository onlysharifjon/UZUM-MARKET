from drf_yasg.utils import swagger_auto_schema
from .models import SalerRegister
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ForLoginSerializer, ForRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class Register(APIView):
    def post(self, request):
        serializer = ForRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "registered"})
        else:
            return Response(serializer.errors)


class SalerLogin(APIView):
    quaryset = SalerRegister
    serializer_class = ForLoginSerializer


def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    name = SalerRegister.objects.filter(login=username, password=password).first()
    return Response({"Login Success": name.id})

#
class SalerLogout(APIView):
    def get(self, request, pk):
        user = SalerRegister.objects.all().filter(id=pk).first()
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({"REFRESH TOKEN": str(refresh)})
        else:
            return Response({"ERRORS": "TOKEN ERROR"})
