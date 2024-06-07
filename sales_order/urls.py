from django.contrib import admin
from django.urls import path , include# type: ignore
from app import views

urlpatterns = [
    path('admin/',admin.site.urls),
    # rota, view responsavel, nome de referencia
    path('',views.home,name='home'),
    path('pedidos',views.pedidos,name='pedidos')
]
