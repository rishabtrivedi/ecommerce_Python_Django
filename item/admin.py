from django.contrib import admin

# Register your models here.
from .models import Category, Item # It will import the Category and Item models from the models.py file

admin.site.register(Category) # It will add Category to the admin page
admin.site.register(Item) # It will add Item to the admin page