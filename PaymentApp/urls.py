from django.urls import path

from .views import CardAdd,AddMoneyView

urlpatterns = [
    path('cardadd/',CardAdd.as_view()),
    path('addmoney',AddMoneyView.as_view())
]