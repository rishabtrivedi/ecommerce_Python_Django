from django.shortcuts import render,redirect
from item.models import Item, Category
# Create your views here.
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] # It will return the first 6 items that are not sold
    categories = Category.objects.all() # It will return all the categories in the database
    return render(request, 'core/index.html', {
        'items': items, 
        'categories': categories}) # It will pass the items and categories to the template

def contact(request):
    return render(request, 'core/contact.html')

def terms(request):
    return render(request, 'core/terms.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) # It will create a new instance of the SignupForm with the data from the request

        if form.is_valid(): # It will check if the form is valid
            form.save() # It will save the user to the database

            return redirect('/login/')
    else:
        form = SignupForm() #

    
    
    return render(request, 'core/signup.html', {
        'form': form
    })