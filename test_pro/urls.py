from django.urls import path
from . import views

urlpatterns = [
    path('com/', views.printname, name="printname"),
]