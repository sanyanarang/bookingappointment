from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    number=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    date=models.CharField(primary_key=True,max_length=30)
    time=models.CharField(max_length=40)
    disease=models.CharField(max_length=40)
    address=models.CharField(max_length=40)


    def __str__(self):
        return self.name
