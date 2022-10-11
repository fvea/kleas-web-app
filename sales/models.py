from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    
class Item(models.Model):
    item = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.item

class Sale(models.Model):
    sales_id = models.AutoField(primary_key=True)
    price = models.FloatField()
    quantity = models.IntegerField(validators=[MinValueValidator(limit_value=1)])
    purchase_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.category}-{self.item}"