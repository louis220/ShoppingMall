from django.urls import path
from . import views

app_name = 'pick'

urlpatterns =[
    path('add/<int:product_id>/', views.add_pick, name='add_pick'),
    path('', views.pick_detail, name ='pick_detail')

]



