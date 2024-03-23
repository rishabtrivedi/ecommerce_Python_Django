from django.db import models
from django.contrib.auth.models import User # It will import the User model from the django.contrib.auth.models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta: # It is used to define the metadata of the model
        ordering = ('name',) # It will order the categories by name
        verbose_name_plural = 'Categories' # It will change the name of the model in the admin page
    
    def __str__(self): # It will return the name of the category
        return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) # on_delete=models.CASCADE will delete all the items in the category if the category is deleted
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # Casacde will delete all the items created by the user if the user is deleted
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name