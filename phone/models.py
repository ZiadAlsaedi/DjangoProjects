from django.db import models

# Create your models here.

class Items(models.Model):
   name=models.CharField(max_length=50)
   def __str__(self):
      return self.name
   
class ItemDetails(models.Model):
   color=models.CharField(max_length=50)
   price=models.FloatField()
   qty=models.IntegerField()
   tax=models.FloatField()
   image=models.CharField(max_length=500,null=True)
   total=models.FloatField()
   date=models.DateTimeField(auto_now_add=True)
   itemsid=models.ForeignKey(Items,on_delete=models.CASCADE)
   def __str__(self):
     return self.color

class Cart(models.Model):
   Id_product=models.IntegerField() 
   Id_user=models.IntegerField() 
   price=models.FloatField()
   qty=models.IntegerField()
   tax=models.FloatField()
   total=models.FloatField()
   discount=models.FloatField()
   net=models.FloatField()
   status=models.BooleanField()
   create_at=models.DateTimeField(auto_now_add=True)
