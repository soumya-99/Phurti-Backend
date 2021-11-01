'''
This file simply does converting our complex types or model instances to native python data types that can be rendered easily into JSON or XML or other content types.

They also help us in seriliazation which is nothing but converting the parts data back to the complex types
'''

from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('categoryName', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'productName',
            'price',
            'productDescription',
            'productCategory'
        )
