from django.contrib import admin
from . models import Booking
from . models import News
# Register your models here.
admin.site.register(Booking)
admin.site.register(News)