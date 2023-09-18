from django.shortcuts import render,HttpResponse
from .models import Item
from django.template import loader

# Create your views here.

def index(request):
    items = Item.objects.all()
    print('Items..........',items)
    context = {

    }
    template = loader.get_template('food/index.html')
    # return HttpResponse('Hello')
    return render(request, 'food/index.html') 
    # return HttpResponse(template.render(context, request))