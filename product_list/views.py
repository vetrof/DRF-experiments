from django.shortcuts import render
from rest_framework import viewsets

from product_list.models import Food, Category
from product_list.serializers import CategorySerializer, FoodSerializer


def list_product(request):
    foods = Food.objects.all().order_by('-id')
    context = {'foods': foods}

    return render(request, 'product_list/index.html', context)


# ---------------- api ----------------------
class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']

    # def create(self, request, *args, **kwargs):
    #     # Логика для обработки метода POST
    #     return super().create(request, *args, **kwargs)


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
