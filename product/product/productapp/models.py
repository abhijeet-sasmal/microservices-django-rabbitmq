from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    image = models.FileField(upload_to="productapp/upload")