from django.db import models


class Dich(models.Model):
    name = models.CharField(max_length=10)
    some1 = models.SmallIntegerField()
    some2 = models.PositiveIntegerField()


class Dich2(models.Model):
    key = models.ForeignKey(Dich, on_delete=models.CASCADE)
    TYPES = (
        (1, 'тип 1'),
        (2, 'тип 2')
    )
    some_types = models.IntegerField(choices=TYPES)


class Product(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    residue = models.PositiveIntegerField()

    def __str__(self):
        return self.title