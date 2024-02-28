from django.urls import path
from vesperrapp import views

urlpatterns = [
    path('',views.home,name="index")
]