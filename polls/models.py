from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True)
