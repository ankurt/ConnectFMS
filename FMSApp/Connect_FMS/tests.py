from django.test import TestCase

import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import User, Building, Location, Utility, Post


class UserModelTests(TestCase):

	def test_string_representation(self):
		user = User.objects.create(andrewid = "slanand")
		self.assertEqual(str(user), user.andrewid)

	def test_default_and_custom_roles(self):
		user1 = User.objects.create(andrewid = "kndu")
		user2 = User.objects.create(andrewid = "slanand", role = "fms")
		user3 = User.objects.create(andrewid = "rdonegan", role = "admin")
		self.assertEqual(user1.role, 'student')
		self.assertEqual(user2.role, 'fms')
		self.assertEqual(user3.role, 'admin')

	def test_ordering_of_users(self):
		user1 = User.objects.create(andrewid = "kndu", first_name = "Katherine", last_name = "Du")
		user2 = User.objects.create(andrewid = "slanand", first_name = "Swathi", last_name = "Anand")
		user3 = User.objects.create(andrewid = "rdonegan", first_name = "Ryan", last_name = "Donegan")
		user3 = User.objects.create(andrewid = "adonegan", first_name = "Allison", last_name = "Donegan")
		results = User.objects.all()
		self.assertEqual(results[0].first_name, 'Swathi')
		self.assertEqual(results[3].first_name, 'Katherine')
		self.assertEqual(results[1].first_name, 'Allison')
		self.assertEqual(results[2].first_name, 'Ryan')

	def test_full_name_function(self):
		user1 = User.objects.create(andrewid = "kndu", first_name = "Katherine", last_name = "Du")
		user2 = User.objects.create(andrewid = "slanand", first_name = "Swathi", last_name = "Anand")
		user3 = User.objects.create(andrewid = "rdonegan", first_name = "Ryan", last_name = "Donegan")
		results = User.objects.all()
		self.assertEqual(user2.full_name(), 'Swathi Anand')
		self.assertEqual(user1.full_name(), 'Katherine Du')
		self.assertEqual(user3.full_name(), 'Ryan Donegan')

	def test_filtering_by_role(self):
		user1 = User.objects.create(andrewid = "kndu", first_name = "Katherine", last_name = "Du")
		user2 = User.objects.create(andrewid = "slanand", first_name = "Swathi", last_name = "Anand", role = "fms")
		user3 = User.objects.create(andrewid = "rdonegan", first_name = "Ryan", last_name = "Donegan", role = "fms")
		user4 = User.objects.create(andrewid = "hyeayouy", first_name = "Jenny", last_name = "Yang")
		user4 = User.objects.create(andrewid = "ajain", first_name = "Aditi", last_name = "Jain", role = "admin")
		fmsUsers = User.fms_users.all()
		studentUsers = User.student_users.all()
		adminUsers = User.admin_users.all()
		self.assertEqual(len(fmsUsers), 2)
		self.assertEqual(len(studentUsers), 2)
		self.assertEqual(len(adminUsers), 1)
		self.assertEqual(fmsUsers[0].first_name, 'Swathi')
		self.assertEqual(fmsUsers[1].first_name, 'Ryan')
		self.assertEqual(studentUsers[0].first_name, 'Katherine')
		self.assertEqual(studentUsers[1].first_name, 'Jenny')


class BuildingModelTests(TestCase):

	def test_string_representation(self):
		building = Building.objects.create(name = "Baker Hall")
		self.assertEqual(str(building), building.name)

	def test_full_address_function(self):
		building = Building.objects.create(name = "Baker Hall", street_1 = '1098 Morewood Avenue', 
											city = "Pittsburgh", state = "PA", zipcode = "15213")
		self.assertEqual(building.full_address(), "1098 Morewood Avenue, Pittsburgh, PA, 15213")

	def test_ordering_of_buildings(self):
		building1 = Building.objects.create(name = "Baker Hall")
		building2 = Building.objects.create(name = "Porter Hall")
		building3 = Building.objects.create(name = "Gates-Hillman Center")
		building4 = Building.objects.create(name = "CUC")
		results = Building.objects.all()
		self.assertEqual(results[0].name, 'Baker Hall')
		self.assertEqual(results[1].name, 'CUC')
		self.assertEqual(results[2].name, 'Gates-Hillman Center')
		self.assertEqual(results[3].name, 'Porter Hall')


class LocationModelTests(TestCase):
	def test_string_representation(self):
		location = Location.objects.create(name = "Danforth")
		self.assertEqual(str(location), location.name)

	def test_foreign_key_building(self):
		building = Building.objects.create(name = "Porter Hall")
		location = Location.objects.create(name = "222", building = building)
		self.assertEqual(location.building.name, "Porter Hall")

	def test_full_location_name_function(self):
		building = Building.objects.create(name = "Porter Hall")
		location = Location.objects.create(name = "222", building = building)
		self.assertEqual(location.full_location_name(), "Porter Hall 222")

	def test_ordering_of_locations(self):
		pass


class UtilityModelTests(TestCase):
	
	def test_string_representation(self):
		utility = Utility.objects.create(name = "Water")
		self.assertEqual(str(utility), utility.name)

	def test_verbose_name_plural(self):
		self.assertEqual(str(Utility._meta.verbose_name_plural), "utilities")

	def test_ordering_of_utilities(self):
		utility1 = Utility.objects.create(name = "Water")
		utility2 = Utility.objects.create(name = "Lights")
		utility3 = Utility.objects.create(name = "Heating systems")
		utility4 = Utility.objects.create(name = "Cooling systems")
		utility5 = Utility.objects.create(name = "Electricity")
		results = Utility.objects.all()
		self.assertEqual(results[0].name, 'Cooling systems')
		self.assertEqual(results[1].name, 'Electricity')
		self.assertEqual(results[2].name, 'Heating systems')
		self.assertEqual(results[3].name, 'Lights')
		self.assertEqual(results[4].name, 'Water')


class PostModelTests(TestCase):

	def test_ordering_of_posts(self):
		utility = Utility.objects.create(name = "Water")
		building = Building.objects.create(name = "Porter Hall")
		location = Location.objects.create(name = "222", building = building)
		user1 = User.objects.create(andrewid = "kndu", first_name = "Katherine", last_name = "Du")
		user2 = User.objects.create(andrewid = "slanand", first_name = "Swathi", last_name = "Anand")
		user3 = User.objects.create(andrewid = "rdonegan", first_name = "Ryan", last_name = "Donegan")
		post1 = Post.objects.create(user = user1, utility = utility, location = location, votes = 2)
		post2 = Post.objects.create(user = user2, utility = utility, location = location)
		post3 = Post.objects.create(user = user2, utility = utility, location = location, votes = 4)
		results = Post.objects.all()
		self.assertEqual(results[0].votes, 4)
		self.assertEqual(results[1].votes, 0)
		self.assertEqual(results[2].votes, 2)


class FormValidation(TestCase):

	def test_user_form(self):
		pass

	def test_building_form(self):
		pass

	def test_location_form(self):
		pass

	def test_utility_form(self):
		pass

	def test_post_form(self):
		pass













