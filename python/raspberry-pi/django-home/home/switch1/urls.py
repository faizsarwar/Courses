from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('on/',views.on,name="on"),
    path('off/',views.off,name="off")
]