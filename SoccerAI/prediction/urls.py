from django.urls import path
from . import views

urlpatterns = [
    path('', views.prediction, name='predcition'),
    path('expresspool/', views.expresspool, name='expresspool'),
]