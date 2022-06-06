from .import views
from django.urls import path


urlpatterns = [
    path('title/', views.home, name='home')
]
