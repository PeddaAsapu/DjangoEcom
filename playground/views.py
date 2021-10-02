from django.shortcuts import render
#from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product,Cart,CartItem,Order,OrderItem
from tags.models import TaggedItem

# Create your views here.

"""
To get the objects from database 

Tablename.objects.all() - to get all data from table
Tablename.objects.get(id = something) - to get particular record
Tablename.objects.filter(condition) - to get based on condition

To insert to table :




"""


def say_hello(request):

    # ...
    queryset = Product.objects.raw('select id,title from store_product')


    return render(request,'hello.html',{'name' : 'surya', 'result': list(queryset)})