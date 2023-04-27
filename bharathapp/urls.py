from django.urls import path

from bharathapp.views import index

urlpatterns = [
    path('',index,name="index"),
]
