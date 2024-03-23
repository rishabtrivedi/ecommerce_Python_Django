from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-3 px-4 rounded-md border focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent'
 # It will define the classes that will be used to render the form fields

class NewItemForm(forms.ModelForm): # It will create a new form class that will be used to create a new item
    class Meta: # It will define the fields that will be used in the form
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            # It will define the widgets that will be used to render the form fields
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES 
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm): # It will create a new form class that will be used to edit an item
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }