from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from polymorphic import PolymorphicModel
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.files import File
import datetime


ROLE_CHOICES = (
    ('admin', 'Administrator'), 
    ('student', 'Student'), 
    ('fms', 'FMS')
    )

STATUS_CHOICES = (
    (1, 'not resolved'), 
    (2, 'in progress'),
    (3, 'resolved')
    )

STATES_CHOICES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connectict'), ('DE', 'Delaware'), ('DC', 'District of Columbia '), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin '), ('WY', 'Wyoming'))


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(
        max_length = 15, 
        blank = False, 
        choices = ROLE_CHOICES,
        default = 'student')
    image = models.ImageField(upload_to = "images/profilepics/%Y/%m/%d", blank = True)

    def addStudentPermissions():
        userobject = django.contrib.auth.get_user_model().objects.get(id=self.user)
        permissions = [
            ('Can add post'), ('Can change post'), ('Can delete post'), 
            ('Connect_FMS.permission.can_add_post_comment'), ('Can change post comment'), ('Can delete post comment'),
            ('Can add status comment'), ('Can change status comment'), ('Can delete status comment'),
            ('Can add likes'), ('Can change likes'), 
            ('Can add votes'), ('Can change votes'),
            ]
        userobject.user_permissions.add(permissions)
        return

    def addFMSPermissions():
        userobject = django.contrib.auth.get_user_model().objects.get(id=self.user)
        permissions = [
            ('Can add status'), ('Can change status'), ('Can delete status'), 
            ('Can add post comment'), ('Can change post comment'), ('Can delete post comment'),
            ('Can add status comment'), ('Can change status comment'), ('Can delete status comment'),
            ]
        userobject.user_permissions.add(permissions)
        return


class Building(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    street = models.CharField(max_length=300, blank = True)
    zipcode = models.CharField(
        max_length = 300,
        blank = False,
        validators = [RegexValidator(r'^[0-9]{5}$', "Only digits 0-9 are allowed.", "Invalid zipcode")])
    city = models.CharField(max_length=100, blank = True)
    state = models.CharField(max_length = 2, choices = STATES_CHOICES, default = 'PA', blank = True)

    def __str__(self):
        return self.name

    def full_address(self):
        return '%s, %s, %s, %s' % (self.street, self.city, self.state, self.zipcode)

    class Meta:
        ordering = ["name"]


class Location(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    building = models.ForeignKey(Building, null = True, blank = True)
    description = models.CharField(max_length=600, blank = True)

    def __str__(self):
        return self.building.name + " " + self.name

    class Meta:
        ordering = ["building__name"]


class Utility(models.Model):
    name = models.CharField(max_length = 30, blank = False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "utilities"


class FMSPostManager(models.Manager):
    def get_queryset(self):
        return super(FMSUserManager, self).get_queryset().filter(votes__gte=10).order_by('-created_at', 'votes')

class Post(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)
    description = models.CharField(max_length = 200, blank = False)
    utility = models.ForeignKey(Utility)
    image = models.ImageField(upload_to = 'images/posts/%Y/%m/%d', blank = True, null = True)
    objects = models.Manager() # default manager
    FMS_posts = FMSPostManager() # posts for FMS to view

    def numcomments(self):
        return PostComment.objects.filter(post=self.id).count()

    # def percentvotes(self):
    #     votes_threshold = 50
    #     return int((float(Votes.objects.get(post=self.id).vote)/float(votes_threshold))*100)

    def getcomments(self):
        return PostComment.objects.filter(post=self.id).all()

    def getresponse(self):
        return Response.objects.filter(post=self.id).all()

    def numvotes(self):
        votes = Votes.objects.filter(post=self.id).all()
        numvote = 0
        for vote in votes:
            numvote += vote.vote
        return numvote

    class Meta:
        ordering = ["-created_at"]

class Votes(models.Model):
    VoteChoices = (
        (1, 'upvote'),
        (0, 'novote'),
        (-1, 'downvote')
    )

    vote = models.IntegerField(default=0, choices=VoteChoices)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)


class Status(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length = 600, blank = False)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)
    image = models.ImageField(upload_to = 'images/statuspics/%Y/%m/%d', blank = True, null = True)
    utility = models.ForeignKey(Utility)
    numlikes = models.IntegerField(default = 0)

    class Meta:
        ordering = ["-created_at"]

    def getcomments(self):
        return StatusComment.objects.filter(status=self.id).all()

    def numcomments(self):
        return StatusComment.objects.filter(status=self.id).count()

    # def like(status):
    #     status.likes+= 1
    #     status.save(update_fields=["likes"])
    # return

class Likes(models.Model):
    like = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)


class Response(models.Model):
    post = models.ForeignKey(Post, null = True, blank = True)
    status = models.ForeignKey(Status, null = True, blank = True)
    status_level = models.IntegerField(
        blank = True,
        choices = STATUS_CHOICES,
        default = 1)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)


class Comment(PolymorphicModel):
    user = models.ForeignKey(User)
    description = models.CharField(max_length = 600)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)

    class Meta:
        ordering = ["created_at"]

class StatusComment(Comment):
    status = models.ForeignKey(Status)

class PostComment(Comment):
    post = models.ForeignKey(Post)



