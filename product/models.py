from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_qty = models.IntegerField()
    product_color = models.CharField(max_length=50,null=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=50)    
    category_description = models.TextField()
    class Meta:
        db_table = 'category'