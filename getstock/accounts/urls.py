


from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login,name = "accounts_login"),
    path("register/", views.register,name = "accounts_register"),

    path("all/", views.all, name = "accounts_all"),
    path("all/<str:login>", views.user, name = "accounts_user"),

    ]
