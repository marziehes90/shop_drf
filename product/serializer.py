from rest_framework import serializers
from .models import Brand,Category,Product,ProductLine

class BrandSerializer(serializers.ModelSerializer):
   brand_name=serializers.CharField(source="name")
     
   class Meta:
      model=Brand
      fields=["brand_name"]

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta:
      model=Category
      fields=["name"]

class ProductLineSerializer(serializers.ModelSerializer):

   class Meta:
      model=ProductLine
      fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
   brand_name=serializers.CharField(source="brand.name")
   category_name=serializers.CharField(source="category.name")
   product_line=ProductLineSerializer(many=True)
   
   class Meta:
      model=Product
      fields=["brand_name","category_name","product_line","name","description","is_digital"]

