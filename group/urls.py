from django.urls import include, path
from group import views 

urlpatterns = [

    path('add/',views.group),
    path('contactus/', views.contactus),
    path('aboutus/', views.aboutus),
    path('',views.index),
    
]
