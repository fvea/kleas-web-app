from random import choices
from unicodedata import category
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Sale(models.Model):

    ITEM = [
        ('Adult Men', (
                ('polo', 'Polo'),
                ('sando', 'Sando'),
                ('short', 'Short'),
                ('t-shirt', 'T-shirt'),
                ('hoodie', 'Hoodie'),
            )
        ),
        ('Adult Women', (
                ('t-shirt', 'T-shirt'),
                ('dress', 'Dress'),
                ('crop-top', 'Crop Top'),
                ('blouse', 'Blouse'),
                ('pants', 'Pants'),
                ('terno', 'Terno'),
                ('skirts', 'Skirts'),
                ('hoodie', 'Hoodie'),
            )
        ),
        ('Child Boys', (
                ('t-shirt', 'T-shirt'),
                ('pants', 'Pants'),
                ('terno', 'Terno'),
            )
        ),
        ('Child Girls', (
                ('t-shirt', 'T-shirt'),
                ('pants', 'Pants'),
                ('skirts', 'Skirts'),
                ('terno', 'Terno'),
                ('onesie', 'Onesie'),
                ('dress', 'Dress')
            )
        ),
    ]

    sales_id = models.AutoField(primary_key=True)
    price = models.FloatField()
    quantity = models.IntegerField(validators=[MinValueValidator(limit_value=1)])
    purchase_date = models.DateTimeField(auto_now_add=True)

    item = models.fields.CharField(max_length=20, choices=ITEM)

    def __str__(self):
        return f'{self.sales_id} @ {self.purchase_date}'

    

