from django.shortcuts import render
from rest_framework import viewsets

from product_list.models import Food, Category
from product_list.serializers import CategorySerializer, FoodsSerializer


def list_product(request, category=None):
    if category is None:
        foods = Food.objects.all().order_by('-id')
        context = {'foods': foods}

    else:
        foods = Food.objects.filter(cat=category)
        context = {'foods': foods}

    cat = Category.objects.all()

    context['cat'] = cat
    return render(request, 'product_list/index.html', context)


# ---------------- api ----------------------
class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']


class FoodsApi(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodsSerializer
