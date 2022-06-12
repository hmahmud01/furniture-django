from os import name
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from website import views

urlpatterns = [
    path('', views.home, name="home"),
    path('area/', views.area, name="area"),
    path('shoplist/<int:aid>/', views.shoplist, name="shoplist"),
    path('furnitures/<int:sid>/', views.furnitures, name="furnitures"),
    path('order/', views.orderFunitures, name="order"),
    path('listoforders/', views.listOfOrders, name="listoforders"),
    path('orderdetail/<int:oid>', views.orderDetails, name="orderdetail"),
    path('detail/<int:fid>/', views.detail, name="detail"),    
    path('print/<int:fid>/', views.printDoc, name="print"),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
