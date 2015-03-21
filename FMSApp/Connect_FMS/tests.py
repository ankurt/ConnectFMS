from django.test import TestCase

import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import User, Building, Location, Post

# def create_question(question_text, days):
# 	time = timezone.now() + datetime.timedelta(days=days)
# 	return Question.objects.create(question_text = question_text, pub_date=time)
		

# Create your tests here.
def createUser(andrewid, firstname, lastname, email, role):
	return User.objects.create(
		andrewid = andrewid, 
		first_name = firstname, 
		last_name = lastname, 
		email = email,
		role = role)

def createBuilding(name, street_1, zipcode, state):
	return Building.objects.create(
		name = name,
		street_1 = street_1,
		zipcode = zipcode,
		state = state)

def createLocation(name, building, description):
	return Location.objects.create(
		name = name,
		building = building,
		description = description)

class UserModelTests(TestCase):
	pass

class BuildingModelTests(TestCase):
	pass

class LocationModelTests(TestCase):
	pass

class PostModelTests(TestCase):
	pass


