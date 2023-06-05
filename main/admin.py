from django.contrib import admin
from main.models import Brand, Model, Car, Person

# Register your models here.
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Person)