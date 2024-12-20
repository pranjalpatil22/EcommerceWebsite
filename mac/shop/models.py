from django.db import models

# Creat e your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=500,default="")
   

    def __str__(self):
        return self.name
    

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=40)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default="0")
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField
    itemsJson = models.TextField(default='')
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100,)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name
    