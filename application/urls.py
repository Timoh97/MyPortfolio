from django.urls import path
from . import views



urlpatterns = [
path('',views.index, name='index'),
path('biodata',views.biodata, name='biodata'),
path('accounts/profile/', views.index, name='index'),
path('project',views.project, name='project'),
]