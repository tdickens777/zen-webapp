from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login-page'),
    path('register/', views.register, name="registration-page")
]
