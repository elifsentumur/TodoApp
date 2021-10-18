# from views import DeveloperList
from . import views
from django.urls import path
app_name ='home'
urlpatterns = [
    path('',views.Index,name="index"),
] 

