from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_expiry_date = models.CharField(max_length=20)
    product_manufacturing_date = models.DateField()
    product_hsn_no = models.CharField(max_length=8)
    product_quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ['product_category']
