from datetime import datetime

from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.now)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)
