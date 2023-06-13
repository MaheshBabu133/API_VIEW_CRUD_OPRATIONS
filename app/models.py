from django.db import models

# Create your models here.

class Prouct_Categeory(models.Model):
    pcid=models.IntegerField()
    pcname=models.CharField(max_length=100)

    def __str__(self):
        return self.pcname

class Product(models.Model):
    pcname=models.ForeignKey(Prouct_Categeory,on_delete=models.CASCADE)
    pid=models.IntegerField()
    pname=models.CharField(max_length=100)
    price=models.FloatField()

    def __str__(self):
        return self.pname
