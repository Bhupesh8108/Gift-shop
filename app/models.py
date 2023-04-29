from django.db import models
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
    category = models.CharField(choices=categories,max_length=20)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.name 