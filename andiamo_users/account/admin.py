from django.contrib import admin

from .models import MyUser, Driver, Owner, Passenger

admin.site.register(MyUser)
admin.site.register(Driver)
admin.site.register(Owner)
admin.site.register(Passenger)