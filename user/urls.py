from django.urls import path
from . import views




urlpatterns = [
    path("",views.user,name="user"),
    path("myrequest/",views.myrequest,name="myrequest"),
    path("newrequest/",views.newrequest,name="newrequest"),
    path("testmsg/",views.testmsg,name="testmsg"),
    path('private_messageu/<int:request_id>/', views.private_messageu, name='private_messageu'),
]

