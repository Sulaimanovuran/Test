from django.urls import path
from applications.category.views import *

urlpatterns = [
    path('', get_category),
]
