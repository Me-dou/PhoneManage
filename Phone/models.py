from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Phone(models.Model):
    brand = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='PhoneCategory', on_delete=models.CASCADE, null=True, blank=True)








