from django.urls import path
from .views import Login, RegstrView,UpdateuserPassword
urlpatterns = [
    path('login/', Login.as_view()), 
    path('register/', RegstrView.as_view()),
    path('update/',UpdateuserPassword.as_view())
    # path('logout/', LogOut.as_view()),
]
