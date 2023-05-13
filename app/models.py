from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator,MinValueValidator
import os,datetime
from django.utils import timezone
categories = [
    ('Birthday', 'hbd'),
    ('Electronic','elt'),
    ('Anniversary','anv'),
    ('Flowers','flw'),
    ('Chocolate','clt'),
    ('Jewels','jwl')
]
options = {
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Delivered','Delivered'),



}
def upload_path(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    return 'app/images/product/{}{}'.format(base_filename, file_extension)

class item(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=56,default = None)
    description = models.CharField(max_length=500,default = " Good quality product")
    image = models.ImageField(upload_to=upload_path)
    price = models.IntegerField()
    offer_price = models.IntegerField(default=0)
    category = models.CharField(choices=categories,max_length=20)
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE ,default="26")

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
    phone_number = models.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(9000000000)])
    def __str__ (self):
        return f'{self.name} {self.user}  {self.country}'
    

class order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    address = models.ForeignKey(customer,on_delete=models.CASCADE)
    product = models.ForeignKey(item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=10,choices=options,default='Pending')
    def __str__(self):
        return f'{self.product} by {self.user}Rs.{self.price}'


class search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    searchtext = models.TextField()
    ip = models.TextField(default="0.0.0.0")
    datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.searchtext} by {self.user}'
    
class forget_password(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        forgot_password_token = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now = True)
        def __str__(self):
            return str(self.user)