from django.db import models

from authentification.models import User

# Create your models here.


class Product(models.Model):
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    nutriscore_grade = models.CharField(max_length=8)
    fatty_acids = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    saturated_fatty_acids = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    sugar = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    salt = models.DecimalField(max_digits=8, decimal_places=3, null=True)
    image = models.URLField(max_length=200, null=True)
    url = models.URLField(max_length=200, null=True)
    relation_user = models.ManyToManyField(User, through='Favorites')

    def __str__(self):
        return self.name


class Favorites(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)

    def __str__(self):
        return self.user.email
