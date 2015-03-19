from django.db import models

class User(models.Model):
    andrewid = models.CharField(
        max_length = 20,
        required = True)
    first_name = models.CharField(
        max_length = 50,
        required = True
        )
    last_name = models.CharField(
        max_length = 50,
        required = True
        )
    email = models.CharField(
        max_length = 100,
        required = True)
    
    roles = [['admin', 'Administrator'], ['student', 'Student'], ['fms', 'FMS']]
    role = models.CharField(
        max_length = 15,
        choices = roles, 
        default = 'student'
        required = True)

    def __str__(self):
        return self.first_name + self.last_name

     def save(self, force_insert=False, force_update=False):
        self.first_name = self.name.capitalize()
        self.last_name = self.name.capitalize()
        self.andrewid = self.name.lower()
        self.email = self.name.lower()
        super(State, self).save(force_insert, force_update)

# class Building(models.Model):
#     name = models.CharField(max_length=50)
#     street_1 = models.CharField(max_length=300)
#     zipcode = models.CharField(max_length=300)

#     states_choices = [['AL', 'Alabama'], ['AK', 'Alaska'], ['AZ', 'Arizona'], ['AR', 'Arkansas'], ['CA', 'California'], ['CO', 'Colorado'], ['CT', 'Connectict'], ['DE', 'Delaware'], ['DC', 'District of Columbia '], ['FL', 'Florida'], ['GA', 'Georgia'], ['HI', 'Hawaii'], ['ID', 'Idaho'], ['IL', 'Illinois'], ['IN', 'Indiana'], ['IA', 'Iowa'], ['KS', 'Kansas'], ['KY', 'Kentucky'], ['LA', 'Louisiana'], ['ME', 'Maine'], ['MD', 'Maryland'], ['MA', 'Massachusetts'], ['MI', 'Michigan'], ['MN', 'Minnesota'], ['MS', 'Mississippi'], ['MO', 'Missouri'], ['MT', 'Montana'], ['NE', 'Nebraska'], ['NV', 'Nevada'], ['NH', 'New Hampshire'], ['NJ', 'New Jersey'], ['NM', 'New Mexico'], ['NY', 'New York'], ['NC', 'North Carolina'], ['ND', 'North Dakota'], ['OH', 'Ohio'], ['OK', 'Oklahoma'], ['OR', 'Oregon'], ['PA', 'Pennsylvania'], ['RI', 'Rhode Island'], ['SC', 'South Carolina'], ['SD', 'South Dakota'], ['TN', 'Tennessee'], ['TX', 'Texas'], ['UT', 'Utah'], ['VT', 'Vermont'], ['VA', 'Virginia'], ['WA', 'Washington'], ['WV', 'West Virginia'], ['WI', 'Wisconsin '], ['WY', 'Wyoming']]
#     state = models.CharField(max_length=2, choices=states_choices,default='PA')

#     def __str__(self):
#         return self.name

# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     building = models.ForeignKey(Building)
#     description = models.CharField(max_length=600)
#     # latitude = models.IntegerField(default=0)
#     # latitude = models.IntegerField(default=0)

#     def __str__(self):
#         return self.name

#     def full_location_name(self):
#         if self.building != NULL: 
#             return self.building.name + self.name

# class Utility(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     user = models.ForeignKey(User)
#     location = models.ForeignKey(Location)
#     datetime = models.DateTimeField(auto_now_add=True)
#     votes = models.IntegerField(default=0)
#     description = models.CharField(max_length=200)
#     utility = models.ForeignKey(Utility)
#     image = models.CharField(max_length=200)
#     title = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title

#     # def up_vote(post):
#     #     post.votes+= 1
#     #     post.save(update_fields=["votes"])
#     # return

#     # def down_vote(post):
#     #     post.votes-= 2
#     #     post.save(update_fields=["votes"])
#     # return

# class Status(models.Model):
#     user = models.ForeignKey(User)
#     description = models.CharField(max_length=600)
#     image = models.CharField(max_length=900)
#     datetime = models.DateTimeField(auto_now_add=True)
#     utility = models.ForeignKey(Utility)
#     title = models.CharField(max_length=50)
#     likes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.title

#     # def up_like(status):
#     #     status.likes+= 1
#     #     status.save(update_fields=["likes"])
#     # return

# class Response(models.Model):
#     post = models.ForeignKey(Post)
#     status = models.ForeignKey(Status)
#     status_level = models.IntegerField(default=0)
#     datetime = models.DateTimeField(auto_now_add=True)

# class Comment(models.Model):
#     user = models.ForeignKey(User)
#     description = models.CharField(max_length=600)
#     datetime = models.DateTimeField(auto_now_add=True)
#     # type_of_post = models.CharField(max_length=50)
#     # type_of_post_id = models.ForeignKey


# # def determine_status(post):
# #     if(post.votes > 50)

# #     return




