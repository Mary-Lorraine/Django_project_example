# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from analysis.models import (
    StockName, StockPrices
)

# Register your models here.

@admin.register(StockName, StockPrices)
class StocksAdmin(admin.ModelAdmin):
    pass