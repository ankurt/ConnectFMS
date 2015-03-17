from django.db import models
from 

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
    utility = models.ForeignKey(Utility)
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=50)

class Location(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building)
    description = models.CharField(max_length=600)
    # latitude = models.IntegerField(defaul=0)
    # latitude = models.IntegerField(default=0)

class Utility(models.Model):
    name = models.CharField(max_length=30)

class Comment(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=600)
    datetime = models.DateTimeField(auto_now_add=True)
    # type_of_post = models.CharField(max_length=50)
    # type_of_post = models.ForeignKey

class Building(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)

class Response(models.Model):
    post = models.ForeignKey(Post)
    status = models.ForeignKey(Status)
    status_level = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

class Status(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=600)
    image = models.CharField(max_length=900)
    datetime = models.DateTimeField(auto_now_add=True)
    utility = models.ForeignKey(Utility)


# def up_vote(post):
#     post.votes+= 1
#     return

# def down_vote(post):
#     if(post.votes > 0):
#         post.votes-= 5
#     return

# def determine_status(post):
#     if(post.votes > 50)

#     return
