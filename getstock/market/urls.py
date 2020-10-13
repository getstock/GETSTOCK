


from django.urls import path
from . import views

urlpatterns = [
    path("stock_info/<str:stock_name>", views.info,name = "info"),
    path("buy_cost/", views.buy,name = "stock_buy_cost"),
    path("all/", views.all, name = "all"),
    path("sell_cost", views.sell, name = "stock_sell_cost"),

    ]
