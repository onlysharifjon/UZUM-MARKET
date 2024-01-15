from django.shortcuts import render
from .models import ProductModel
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AllProductSerializer
from .paginations import LargeResultsSetPagination
class AllProductView(APIView):
    pagination_class = LargeResultsSetPagination
    def get(self,request):
        datas = ProductModel.objects.all()
        serializer = AllProductSerializer(datas,many=True)
        return Response(serializer.data)


# Create your views here.
