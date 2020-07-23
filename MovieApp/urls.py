from .views import person_list, movie_list,person_detail,movie_detail, add_person,add_movie,update_person,update_movie
from django.urls import path, include

urlpatterns = [
    path('person/', person_list),
    path('movie/', movie_list),

    path('person/add', add_person),
    path('movie/add', add_movie),


    path('person/detail/<int:id>', person_detail),
    path('movie/detail/<int:id>', movie_detail),

    path('person/<int:id>/', update_person),
    path('movie/<int:id>', update_movie),
]

''''
GET person/
GET person/detail
POST person/add
PUT person/<id>
DELETE person/<id>
'''

