from django.urls import path
from .views import AllProductView

urlpatterns = [
    path('all_product/',AllProductView.as_view())
]