from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    def __str__(self):
        return self.categoryName

class Product(models.Model):
    productName = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    productDescription = models.TextField()
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.productName