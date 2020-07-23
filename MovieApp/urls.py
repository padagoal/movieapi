from .views import person_list, movie_list,person_detail,movie_detail,index
from django.urls import path, include

urlpatterns = [
    path('',index),
    path('person/', person_list),
    path('movie/', movie_list),

    path('person/<int:id>', person_detail),
    path('movie/<int:id>', movie_detail),
]


