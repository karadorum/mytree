from django.db import models


class Category(models.Model):
    """
    вот эта модель должна быть построена по иерархии. Нашел репозиторий который как раз решает эту задачу https://bitbucket.org/larsyencken/django-hierarchy/wiki/Home
    он не очень легкий, но разбирая его по частям, можно попробовать повторить + добавить templatetags
    """
    title = models.CharField(max_length=200)
    left_visit = models.IntegerField(db_index=True)
    right_visit = models.IntegerField(db_index=True)

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True)
