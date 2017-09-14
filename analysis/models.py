# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StockName(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StockPrices(models.Model):
    stock_id = models.ForeignKey(StockName, on_delete=models.CASCADE)
    stock_date = models.DateTimeField()
    stock_open = models.DecimalField(max_digits=20, decimal_places=2)
    stock_high = models.DecimalField(max_digits=20, decimal_places=2)
    stock_low = models.DecimalField(max_digits=20, decimal_places=2)
    stock_close = models.DecimalField(max_digits=20, decimal_places=2)
    stock_volume = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.stock_id)
