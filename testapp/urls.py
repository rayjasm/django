from django.urls import path
from . import views,models

urlpatterns = [
    path("", views.index, name='index'),
    path("", models.exam, name='exam'),
]