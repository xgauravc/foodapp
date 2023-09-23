from django.shortcuts import render,HttpResponse
from .models import Item
from django.template import loader

# Create your views here.

def index(request):
    items = Item.objects.all()
    print('Items..........',items)

    template = loader.get_template('food/index.html')
    # return HttpResponse('Hello')
    return render(request, 'food/index.html', {'item_list':items}) 
    # return HttpResponse(template.render(context, request))


def details(request, item_id):
    item = Item.objects.get(pk= item_id)
    context = {
        'item':item
    }
    # return HttpResponse(f"This is id {item_id}")
    return render(request, 'food/details.html',context)  