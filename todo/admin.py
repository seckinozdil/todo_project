import imp
from django.contrib import admin
from .models import TODOS

# Register your models here.

admin.site.register(TODOS)
