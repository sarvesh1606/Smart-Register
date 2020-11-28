from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.apiOverview,name='api'),
    path('userlist/', views.userList, name="userlist" ),
    path('userspecific/<str:sk>/', views.userSpecific, name="userspecific" ),
    path('usercreate/', views.userCreate, name="usercreate" ),
    path('userupdate/<str:sk>/', views.userUpdate, name="userupdate" ),
    path('userdelete/<str:sk>/', views.userDelete, name="userdelete" ),

]
