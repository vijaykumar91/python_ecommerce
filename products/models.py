from django.db import models


# Create your models here.
class products(models.Model):
    product_category = models.IntegerField()
    product_sub_category = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_short_description = models.CharField(max_length=255)
    product_SKU = models.CharField(max_length=100)
    product_full_description = models.CharField(max_length=100)
    product_additional_info = models.CharField(max_length=100)
    product_image = models.CharField(max_length=255)
    def __str__(self):
        return self.products