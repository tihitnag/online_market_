from django.shortcuts import render,redirect
from item.models import Catagory,Item #inportm the data base 
from .form import SignupForm




    
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]#show top 6 newest items
    catagories=Catagory.objects.all()
    return render(request,'core/index.html',{ # this are the context to use them in the template 
        'catagories':catagories,
        'items':items,
    })
def contact(request):
    return render(request,'core/contact.html')



def signup(request):
    
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')  # Use the name of your login URL pattern
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form,
        'title': 'new item',
    })