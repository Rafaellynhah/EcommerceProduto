from django.urls import path
from produto import views


urlpatterns = [
    path('deposito', views.deposito, name="deposito"),

]
