from django.db import models
from django.template.defaultfilters import default, slugify

# Create your models here.

class Resto(models.Model):
    name = models.CharField(max_length=250)
    location = models.TextField()
    image = models.ImageField()
    description = models.TextField()
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Owner(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField()

# class User(models.Model):
#     username = models.CharField(max_length=250)
#     email = models.EmailField()
#     password = models.CharField(max_length=250)

class item(models.Model):
    hotel = models.CharField(max_length=250)
    food = models.CharField(max_length=250)
    price = models.IntegerField(default=100)

    # def __iter__(self):
    #     yield[self.hotel, self.food, self.price]

class Comments(models.Model):
    hname = models.CharField(max_length=250)
    comment = models.CharField(max_length=1000)

class Dataa(models.Model):
    name = models.CharField(max_length=100)