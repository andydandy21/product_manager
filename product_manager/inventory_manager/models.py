from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=10)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-detail', kwargs={'pk': self.pk})