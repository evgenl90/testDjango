from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=100)
    username = models.CharField('username', max_length=100)
    email = models.EmailField('email', max_length=254)
    address = models.TextField('address')
    phone = models.CharField('phone', max_length=100)
    website = models.CharField('website', max_length=250)
    company = models.TextField('company')

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=250)
    body = models.TextField('body')



 

 

