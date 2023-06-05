from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(unique=True, max_length=20, verbose_name='Марка')
    country = models.CharField(max_length=20, verbose_name='Страна-производитель')

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(unique=True, max_length=20, verbose_name='Модель')

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, to_field='name')
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING, to_field='name')

    def __str__(self):
        return ' '.join([self.brand.name, self.model.name])


class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=30, verbose_name='Город')

    def __str__(self):
        return self.name
