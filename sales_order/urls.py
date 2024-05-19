
from django.urls import path # type: ignore
from app import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path('',views.home,name='home'),
]
