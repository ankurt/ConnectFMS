from django.db import models

class User(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Post(models.Model):
    user_id = models.ForeignKey(User)
    location_id = models.ForeignKey(Location)
    datetime = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    status = models.Boolean(default=False)
    utility = models.CharField(default='electricty')

class Location(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building)
    description = models.CharField(max_length=600)
    # latitude = models.IntegerField(defaul=0)
    # latitude = models.IntegerField(default=0)


class Comment(models.Model):

class Building(models.Model):


