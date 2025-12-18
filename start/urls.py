from django.urls import path
from . import views
from channels.routing import ProtocolTypeRouter, URLRouter

urlpatterns = [
    path("",views.startup,name="startup"),
     
    path("custom_login/",views.custom_login,name="custom_login"),
    path('logout', views.logout_user, name='logout'),
]
