from django.urls import path
from . import views
urlpatterns = [
    path('', views.getQA, name='index2'),
    path('comprehension/', views.comprehension, name='comprehension')


]