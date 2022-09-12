from django.urls import path
from . import views
urlpatterns = [
    path('', views.translate, name='index'),
    path('translated/', views.translated, name='translated')

]