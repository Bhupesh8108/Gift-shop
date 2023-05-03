from django.db import models
from django.contrib.auth.models import User 
import os
categories = [
    ('Birthday', 'hbd'),
    ('Electronic','elt'),
    ('Anniversary','anv'),
    ('Flowers','flw'),
    ('Chocolate','clt'),
    ('Jewels','jwl')
]
def upload_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return 'app/images/product/{}{}'.format(base_filename, file_extension)

class item(models.Model):
    name = models.CharField(max_length=56,default = None)
    description = models.CharField(max_length=500,default = " Good quality product")
    image = models.ImageField(upload_to=upload_path)
    price = models.IntegerField()
    offer_price = models.IntegerField(default=0)
    category = models.CharField(choices=categories,max_length=20)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return str(f'{self.name}({self.id})')
    


class wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    def __str__(self):
        return f'{self.product} by {self.user}'
    


class customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    main_address = models.CharField(max_length=200)
    street_address= models.CharField(max_length=200)
    additional_address = models.CharField(max_length=200)
    country = models.CharField(max_length=20 , default='unknown')
    phone_number = models.IntegerField()
    def __str__ (self):
      return f'{self.name} {self.user}  {self.country}'