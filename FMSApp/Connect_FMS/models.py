from django.db import models

class User(models.Model):
    andrewid = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=15)


class Post(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    datetime = models.DateTimeField(auto_now_add=True)
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
    user = models.ForeignKey(User)
    description = models.CharField(max_length=600)
    datetime = models.DateTimeField(auto_now_add=True)


class Building(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)


