from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Count, ExpressionWrapper, DecimalField

from store.models import Products, Order, Customers, Collection
import json

# Create your views here.

# def sayHello(request):
#     return HttpResponse("Hello world")

def sayHello(request):

    # queryset = Products.objects.filter(title__icontains="coffee", price__range=(20, 30))
    # queryset = Products.objects.filter(Q(price__gt=20) | ~Q(price__lt=30))
    # queryset = Products.objects.filter(price=F('inventory'))
    # queryset = Products.objects.values('id', 'title', 'description', 'price', 'inventory').filter(pk=F('orderitem__product_id')).distinct().order_by('title')
    # prefetch_related >> many to many related, #select_related >> one to many related
    # queryset = Products.objects.prefetch_related('promotions').select_related('collection').all()
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product')[:5]

    # queryset = Customers.objects.annotate(order_count=Count('order'))
    # queryset = Products.objects.annotate(discounted_price=ExpressionWrapper(F('price') * 0.8, output_field=DecimalField()))

    # collection = Collection.objects.create(title="Abdrew Tate", featured_product_id=1)

    Collection.objects.filter(pk=10).update(featured_product=None)


    # print(list(queryset.values()))
  
    return render(request, 'hello.html', {'country': 'Uganda'})