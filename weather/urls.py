from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<int:id>', views.delete, name='delete'),
]
app_name = 'weather'
