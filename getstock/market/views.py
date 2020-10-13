from django.shortcuts import render

# Create your views here.
from .models import *

def  buy(request):
    pass

def sell(request):
    pass

def info(request, stock_name):
    context = dict()
    stock = Stock.objects.get(stock_name = stock_name)
    context['stock'] = stock
    return render(request, '/Users/dalenamir/Desktop/projects/stocks/stocks/templates/stocks/stock.html', context)

def all(request):
    context = dict()
    stocks = Stock.objects.all()
    context['stocks'] = stocks
    return render(request, '/Users/dalenamir/Desktop/projects/stocks/stocks/templates/stocks/all_stocks.html', context)
