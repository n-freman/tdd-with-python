from django.views.generic import FormView, CreateView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from lists.forms import ExistingListItemForm, ItemForm, NewListForm
from lists.models import Item, List

User = get_user_model()


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(
            for_list=list_,
            data=request.POST
        )
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


class NewListView(CreateView):
    template_name = 'home.html'
    form_class = NewListForm 
    
    def form_valid(self, form):
        list_ = form.save(owner=self.request.user)
        return redirect(list_)


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})


def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})


def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    sharee = request.POST.get('sharee')
    list_.shared_with.add(sharee)
    return redirect(f'/lists/{list_id}/')

