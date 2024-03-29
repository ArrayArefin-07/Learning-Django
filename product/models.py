from django.db import models

# Create your models here.
class laptop(models.Model):
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)
    laptop = models.CharField(max_length=100)
    re_laptop = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    about = models.TextField()
    textarea = models.CharField(max_length=50)
    checkbox = models.CharField(max_length=50)
    ram = models.IntegerField()
    ssd = models.CharField(max_length=50) 
    youtube_chanel = models.BooleanField()
    

