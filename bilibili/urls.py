from django.urls import path

from . import views

app_name="bilibili"

urlpatterns = [
    path('', views.index, name='index'),
    path("down/",views.down,name="down",)
]