from django.contrib import admin
from django.urls import path
from applications.product.views import *

urlpatterns = [
    path('', get_products),

]
