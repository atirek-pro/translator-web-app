from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name='index3'),
    path('generatedblog/', views.generatedblog, name='generatedblog')

]