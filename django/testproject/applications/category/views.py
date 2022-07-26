from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from applications.category.models import Category
from applications.category.serializers import CategorySerializers


@api_view(['GET'])
def get_category(request):
    categories = Category.objects.all()
    serializers = CategorySerializers(categories, many=True)
    return Response(serializers.data)

