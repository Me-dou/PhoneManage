from rest_framework import serializers
from .models import Phone, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PhoneSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), source = 'category', write_only = True)

    class Meta:
        model = Phone
        fields = '__all__'

