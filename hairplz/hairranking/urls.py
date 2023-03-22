from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('take_picture.html', views.take_picture, name='take_picture'),
    path('2nd_index.html', views.second_index, name='2nd_index'),
    path('process_ranking/', views.process_ranking, name='process_ranking'),  # Add this line
]
