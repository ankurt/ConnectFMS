from django.contrib import admin

# Register your models here.
from .models import Building, Location, Utility, Post, PostComment, Votes, Status, Response, StatusComment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from Connect_FMS.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = True

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.register(Building)
admin.site.register(Location)
admin.site.register(Utility)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Votes)
admin.site.register(Status)
admin.site.register(Response)
admin.site.register(StatusComment)

