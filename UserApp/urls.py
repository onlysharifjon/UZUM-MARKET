from django.urls import path
from .views import Login, RegstrView
urlpatterns = [
    path('login/', Login.as_view()), 
    path('register/', RegstrView.as_view()),
    # path('logout/', LogOut.as_view()),
]