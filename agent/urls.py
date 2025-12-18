from django.urls import path
from . import views


urlpatterns = [
    path("",views.agent,name="agent"),
    path("unassigned_requests/",views.unassigned_requests,name="unassigned_requests"),
    path("assigned_requests/",views.assigned_requests,name="assigned_requests"),
    path("my_supports/",views.my_supports,name="my_supports"),
    path("resolved_requests/",views.resolved_requests,name="resolved_requests"),
    path("testmsgage/",views.testmsgage,name="testmsgage"),
    path('logout/', views.logout_agent, name='logout'),
    path("register/",views.register,name="register"),
    path('private_messagea/<int:request_id>/', views.private_messagea, name='private_messagea'),
]

