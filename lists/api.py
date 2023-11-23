import json

from django.http import HttpResponse

from lists.forms import ExistingListItemForm
from lists.models import List, Item


def list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(list_, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return HttpResponse(
            json.dumps({'error': form.get_error()}), # type: ignore
            content_type='application/json',
            status=400
        )
    item_dicts = [
        {'id': item.id, 'text': item.text}
        for item in list_.item_set.all()
    ]
    return HttpResponse(
        json.dumps(item_dicts), # type: ignore
        content_type='application/json'
    )

