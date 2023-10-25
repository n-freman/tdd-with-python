from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all() # type: ignore
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text']) # type: ignore
    return redirect('/lists/the-only-list-in-the-world/')

