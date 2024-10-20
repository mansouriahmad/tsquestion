from django.urls import path
from . import views

urlpatterns = [
    path('submit-projects', views.submit_projects, name='submit-projects'),
]