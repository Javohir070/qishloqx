from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Province)

admin.site.register(SubProvince)

admin.site.register(Pump)
admin.site.register(User)
