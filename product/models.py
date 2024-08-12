from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # phone = models.PositiveBigIntegerField(unique=True, null=True)
    # profile_img = models.ImageField(upload_to='customer_imgs/', null=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


