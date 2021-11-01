from django.shortcuts import render
# We can use it (csrf_exempt) to allow other domains to easily access our API methods
from django.views.decorators.csrf import csrf_exempt
# By other domains, our front-end project, we also need something called JSONParser to parse the incomming data into the data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def categoryAPI(request, id=0):
    # Fetch Data
    if request.method == "GET":
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(
            categories, many=True)  # converted into JSON format
        # The parameter safe=False is basically use to inform Django that what we are trying to convert to JSON format that's actually a valid fromat to be converted and we are fine if there're any issues
        return JsonResponse(categories_serializer.data, safe=False)

@csrf_exempt
def productAPI(request, id=0):
    # Fetch Data
    if request.method == "GET":
        products = Product.objects.all()
        products_serializer = ProductSerializer(
            products, many=True)  # converted into JSON format
        # The parameter safe=False is basically use to inform Django that what we are trying to convert to JSON format that's actually a valid fromat to be converted and we are fine if there're any issues
        return JsonResponse(products_serializer.data, safe=False)


# @csrf_exempt
# def SaveImageFile(request):
#     # We are extracting the uploaded file from the request
#     file = request.FILES["myFile"]
#     file_name = default_storage.save(file.name, file)

#     return JsonResponse(file_name, safe=False)