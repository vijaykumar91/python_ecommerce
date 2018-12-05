from django.db import models

# Create your models here.
class user(models.Model):
      id=models.IntegerField(primary_key=True)
      username=models.CharField(max_length=50)
      password=models.CharField(max_length=100)
      email=models.CharField(max_length=20)
      phone=models.CharField(max_length=15)

      def __str__(self):
          return self.user

class role(models.Model):
      id = models.IntegerField(primary_key=True)
      user_id = models.IntegerField()
      name = models.CharField(max_length=100)
      type = models.IntegerField()

      def __str__(self):
          return self.role

# Create your models here.
class products(models.Model):
    id = models.IntegerField(primary_key=True)
    product_category = models.IntegerField()
    product_sub_category = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    product_short_description = models.CharField(max_length=255)
    product_SKU = models.CharField(max_length=100)
    product_full_description = models.CharField(max_length=100)
    product_additional_info = models.CharField(max_length=100)
    product_image = models.FileField(max_length=255)


    def __str__(self):
        return (self.id, self.product_category,self.product_sub_category,self.product_name,self.product_short_description,self.product_SKU,self.product_full_description,self.product_additional_info,self.product_image)

