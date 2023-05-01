from django.db import models

# Create your models here.
#create the regitration form
class formreg(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30, unique = True)
    phone=models.BigIntegerField()
    User_type = models.BigIntegerField(null=True)
    password=models.CharField(max_length=30)
   
    class Meta:
        db_table="formreg"

class product(models.Model):
    product_tittle = models.CharField(max_length=100)
    pname=models.CharField(max_length=30)
    circlesale=models.CharField(max_length=30)
    image=models.FileField(max_length=300,upload_to='media',blank=True,null=True)
    rate=models.BigIntegerField()
    cutrate=models.BigIntegerField()
    

    class Meta:
        db_table="product"
        
#create the Buy order
class addkart(models.Model):                    
    cemail=models.CharField(max_length=30)
    cnam=models.CharField(max_length=30)
    cpho=models.BigIntegerField()
    cpid=models.BigIntegerField()
    cpname=models.CharField(max_length=30)
    cpimg=models.FileField(max_length=300,upload_to='media',blank=True,null=True)
    cprice=models.DecimalField(max_length=100, default=0, max_digits=7, decimal_places=2)
    corderdate=models.CharField(max_length=30,blank=True,null=True)
    cordercout=models.PositiveIntegerField(default=1)
    ctotal=models.DecimalField(max_length=100, default=0, max_digits=7, decimal_places=2)



    class Meta:
        db_table="addkart"


