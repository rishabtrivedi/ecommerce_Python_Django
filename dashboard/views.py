from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user) # It will return all the items created by the user

    return render(request, 'dashboard/index.html', {
        'items': items,
    })