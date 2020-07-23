from .views import person_list, movie_list,person_detail,movie_detail
from django.urls import path, include

urlpatterns = [
    path('person/', person_list),
    path('movie/', movie_list),

    path('person/<int:id>', person_detail),
    path('movie/<int:id>', movie_detail),
]

''''
GET person/
GET person/detail
POST person/add
PUT person/<id>
DELETE person/<id>
'''

