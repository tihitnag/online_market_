from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Catagory, Item

from .forms   import NewItemForm,EditItemForm
from django.db.models import Q

def items(request):
    qurey=request.GET.get('qurey', '')
    category_id= request.GET.get('category', 0)
    
    
    categories =Catagory.objects.all()
    items = Item.objects.filter(is_sold=False)
    if category_id:
        items=items.filter(category_id=category_id)
    if qurey:
        
        items=items.filter(Q(name__icontains=qurey)| Q(description__icontains=qurey))# if the names contain quarys filter is out 
        
    return render(request, 'item/items.html', {
                                    'items': items,
                                    'qurey':qurey,
                                    'categories':categories,
                                    'category_id':int(category_id)
                                    })  # Corrected syntax

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
        # If the form is not valid, you can handle the errors here and render the form with errors.
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': "new item"
    })
@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        
        form = EditItemForm(request.POST, request.FILES,instance=item)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
        # If the form is not valid, you can handle the errors here and render the form with errors.
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': "edit item"
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    # Check if the request method is POST to avoid accidental deletions via GET requests
    
    item.delete()
        
    return redirect('/')
