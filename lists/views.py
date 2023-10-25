from django.shortcuts import render, redirect
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all() # type: ignore
    return render(request, 'list.html', {'items': items})


def new_list(request):
    list_ = List.objects.create() # type: ignore
    Item.objects.create( # type: ignore
        text=request.POST['item_text'],
        list=list_
    )
    return redirect('/lists/the-only-list-in-the-world/')

