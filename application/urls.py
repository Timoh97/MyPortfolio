from django.urls import path
from . import views



urlpatterns = [
path('',views.index, name='index'),
path('accounts/profile/', views.index, name='index'),
]