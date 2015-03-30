from django.contrib import admin

# Register your models here.
from .models import Building, Location, Utility, User


admin.site.register(Building)
admin.site.register(Location)
admin.site.register(Utility)
admin.site.register(User)