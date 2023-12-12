from django.shortcuts import render
from item.models import Item
from django.contrib.auth.decorators  import  login_required

# Create your views here.
@login_required
def index(request):# we want to get all item that was crested
    items=Item.objects.filter(created_by=request.user)
    return render(request,'dashbored/index.html',{
        'items':items,
    })
