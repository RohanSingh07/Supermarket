from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'supermart'


urlpatterns = [
        # Homepage
        path('',views.Homepage,name='Homepage'),

        # REST API
        # Single API url for all purpose
        path('items/',views.Get_All,name="Get_All"),

]
