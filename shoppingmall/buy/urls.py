
from django.urls import  path

from . import views

app_name = 'buy'

urlpatterns = [

    path('add/int:product_id>/', views.add_buy, name ="add_buy"),
    path('', views.buy_detail, name='buy_detail')

]