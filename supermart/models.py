from django.db import models

choices = (('household','household'),
           ('food','food'),
           ('beverage','beverage'),)
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50,unique=True)
    category = models.CharField(max_length=50,choices=choices,blank=True,null=True)
    sub_category = models.CharField(max_length=50,blank=True,null=True)
    amount = models.FloatField()



