from django.shortcuts import render
from rest_framework.views import APIView
from .services import ForloginSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import SalerRegister
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
