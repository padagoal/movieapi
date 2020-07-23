from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Person,Movies

from .utils import get_json_list,convert_int_to_Roman
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers as rei


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','lastname','firstname','aliases',
                  'is_actor','is_director','is_producer')


class MoviesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id','title','release_year','actors','directors','producer')


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    lastname = serializers.CharField( max_length=255)
    firstname = serializers.CharField( max_length=255)
    aliases = serializers.CharField( max_length=255)
    movies_as_actor = serializers.SerializerMethodField('get_movies_actor')
    movies_as_director = serializers.SerializerMethodField('get_movies_director')
    movies_as_producer = serializers.SerializerMethodField('get_movies_producer')

    def get_movies_actor(self,obj):
        try:
            query = Movies.objects.all().filter(actors__id=obj.id)
            if query:
                data = list( query.values('id','title'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def get_movies_director(self,obj):
        try:
            query = Movies.objects.all().filter(directors__id=obj.id)
            if query:
                data = list(query.values('id', 'title'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def get_movies_producer(self,obj):
        try:
            query = Movies.objects.all().filter(producer__id=obj.id)
            if query:
                data = list(query.values('id', 'title'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """

        return instance


class MoviesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    release_year = serializers.SerializerMethodField('get_roman_numbers')
    actors = serializers.SerializerMethodField('get_actor_movies')
    directors = serializers.SerializerMethodField('get_director_movies')
    producers = serializers.SerializerMethodField('get_producer_movies')

    def get_roman_numbers(self,obj):
        return convert_int_to_Roman(self,obj.release_year)

    def get_actor_movies(self,obj):
        try:
            query = Movies.objects.filter(id=obj.id)
            if query:
                actores = Person.objects.filter(id__in=query.values('actors'))
                data = list(actores.values('id','lastname','firstname','aliases'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def get_director_movies(self,obj):
        try:
            query = Movies.objects.filter(id=obj.id)
            if query:
                actores = Person.objects.filter(id__in=query.values('directors'))
                data = list(actores.values('id','lastname','firstname','aliases'))
                return data
            else:
                return ''
        except Exception as e:
            return ''

    def get_producer_movies(self,obj):
        try:
            query = Movies.objects.filter(id=obj.id)
            if query:
                actores = Person.objects.filter(id__in=query.values('producer'))
                data = list(actores.values('id','lastname','firstname','aliases'))
                return data
            else:
                return ''
        except Exception as e:
            return ''



    def create(self, validated_data):
        """

        """
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """

        """

        return instance

    class Meta:
        model = Movies
        fields = ('id','title','release_year','actors','directors','producers')
