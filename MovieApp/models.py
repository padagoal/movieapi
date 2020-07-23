from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(verbose_name='ID',unique=True,primary_key=True,)
    lastname = models.CharField(verbose_name='Last Name',max_length=255)
    firstname = models.CharField(verbose_name='First Name', max_length=255)
    aliases = models.CharField(verbose_name='Aliases',max_length=255,blank=True,null=True)
    is_actor = models.BooleanField(verbose_name='Is Actor?',default=False)
    is_director = models.BooleanField(verbose_name='Is Director?',default=False)
    is_producer = models.BooleanField(verbose_name='Is Producer?',default=False)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return self.lastname + ' ' +self.firstname

    def ListActorMovies(self):
        data = {
            "movies": list(Movies.objects.all().filter(actors__id=self.id)),
        }
        return data


class Movies(models.Model):
    id = models.AutoField(verbose_name='ID', unique=True,primary_key=True)
    title = models.CharField(verbose_name='Title Movie',max_length=255)
    release_year = models.IntegerField(default=0,verbose_name='Release Year')
    actors = models.ManyToManyField(Person, related_name='actor_movie')
    directors = models.ManyToManyField(Person, related_name='director_movie')
    producer = models.ManyToManyField(Person, related_name='producer_movie')

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title





