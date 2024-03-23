from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Category, Item

# Create your views here.

# This is the view for the items page. It will display all the items in the database.
# It will also filter the items by category and search query.
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        # It will filter the items by category
        items = items.filter(category_id=category_id)

    if query:
        # It will filter the items by name or description that contains the query
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request,pk) :
    item  = get_object_or_404(Item,pk=pk) # It will return the item with the id passed in the url 
    # or a 404 error if the item doesn't exist
    
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3] 
    # It will return the items with the same category as the item in the url

    return render(request,'item/detail.html',
                  {'item':item,
                     'related_items':related_items
                   }
                  )

@login_required
# This is the view for the new item page. It will display the form to create a new item.
def new(request):
    if request.method == 'POST':
        # It will create a new instance of the NewItemForm with the data from the request
        form = NewItemForm(request.POST, request.FILES) #

        if form.is_valid():
            # commit=false as required to set the created_by field to the current user
            item = form.save(commit=False) # It will create a new item with the data from the form
            item.created_by = request.user # It will set the created_by field to the current user
            item.save() # It will save the item to the database

            return redirect('item:detail', pk=item.id) 
    else: 
        form = NewItemForm() 

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        # instance will set the form to edit the item with the id passed in the url
        form = EditItemForm(request.POST, request.FILES, instance=item) 

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item) # It will create a new instance of the EditItemForm with the data from the item

    
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')