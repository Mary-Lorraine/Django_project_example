# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect

from models import StockName, StockPrices
from django.shortcuts import render

from django.views.generic import View, ListView, TemplateView


# Create your views here.
class StockList(View):
    stocks = StockName.objects.all()
    template_name='analysis/viewresults.html'
    def get( self, request):
        stocks = self.stocks
        assert isinstance(self.stocks, object)
        return render(request, self.template_name, {'stocks': stocks})

class StockDetails(View):
    def get( self,request):
        diff_percentage = []
        stockid = int(request.GET['id'])
        stock = StockName.objects.get(pk=stockid)
        prices = StockPrices.objects.filter(stock_id=stockid)
        volumelist = prices.order_by('stock_volume')[:5]
        for price in prices:
            diff_percentage.append(price.stock_close - price.stock_open)
        return render(request,"analysis/stockdetails.html", {'prices':prices,'diff_percentage': diff_percentage,'stock':stock,'volumelist':volumelist})
