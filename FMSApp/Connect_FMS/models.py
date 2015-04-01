from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

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


class FMSUserManager(models.Manager):
    def get_queryset(self):
        return super(FMSUserManager, self).get_queryset().filter(role='fms').order_by('last_name', 'first_name')

class StudentUserManager(models.Manager):
    def get_queryset(self):
        return super(StudentUserManager, self).get_queryset().filter(role='student').order_by('last_name', 'first_name')

class AdminUserManager(models.Manager):
    def get_queryset(self):
        return super(AdminUserManager, self).get_queryset().filter(role='admin').order_by('last_name', 'first_name')

class User(models.Model):
    andrewid = models.CharField(max_length = 20, blank = False)
    first_name = models.CharField(max_length = 50, blank = False)
    last_name = models.CharField(max_length = 50, blank = False)
    email = models.EmailField(max_length = 100, blank = False)
    role = models.CharField(
        max_length = 15, 
        blank = False, 
        choices = ROLE_CHOICES,
        default = 'student')

    objects = models.Manager() # default manager
    fms_users = FMSUserManager() # fms users
    student_users = StudentUserManager() # student users
    admin_users = AdminUserManager() # student users

    def __str__(self):
        return self.andrewid 

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ["last_name", "first_name"]


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
    # latitude = models.IntegerField(default=0)
    # latitude = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def full_location_name(self):
        if self.building != None: 
            return self.building.name + " " + self.name

    # # 
    # class Meta:
    #     ordering = ["building.name", "name"]


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
    votes = models.IntegerField(default = 0)
    description = models.CharField(max_length = 200, blank = False)
    utility = models.ForeignKey(Utility)
    image = models.ImageField(upload_to = 'images/posts/', blank = True, null = True)

    objects = models.Manager() # default manager
    FMS_posts = FMSPostManager() # posts for FMS to view

    class Meta:
        ordering = ["-created_at", "-votes"]


class Status(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length = 600, blank = False)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)
    image = models.ImageField(upload_to = 'images/statuses/', blank = True, null = True)
    utility = models.ForeignKey(Utility)
    likes = models.IntegerField(default = 0)

    class Meta:
        ordering = ["-created_at", "likes"]

    # def like(status):
    #     status.likes+= 1
    #     status.save(update_fields=["likes"])
    # return


class Response(models.Model):
    post = models.ForeignKey(Post, null = True, blank = True)
    status = models.ForeignKey(Status, null = True, blank = True)
    status_level = models.IntegerField(
        blank = True,
        choices = STATUS_CHOICES,
        default = 1)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)


class Comment(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length = 600)
    created_at = models.DateTimeField(auto_now_add = True, editable = False)
    # type_of_post = models.CharField(max_length=50)
    # type_of_post_id = models.ForeignKey

    class Meta:
        ordering = ["created_at"]






