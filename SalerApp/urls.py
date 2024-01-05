from django.urls import path
from .views import Register, SalerLogin, SalerLogout

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', SalerLogin.as_view()),
    path('logout/', SalerLogout.as_view()),
]
