from django.contrib import admin
from .models import Address, Student

admin.site.register([Address, Student])
