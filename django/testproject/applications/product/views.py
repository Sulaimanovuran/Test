from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from applications.product.models import Product
from applications.product.serializers import ProductSerializers


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializers = ProductSerializers(products, many=True)

    return Response(serializers.data)
