from django.urls import path
from .views import *
from projectapp.auth.login import user_login
from projectapp.auth.register import register



urlpatterns = [
   
    path('index/',index,name='index'),
    path('createpump/',create_pump,name='create_pump'),
    path('semantic/',semantik,name='semantik'),
    path('get_province',get_province,name='get_province'),
    # path('malumotbir/',create_pump,name='create_pump'),
    
    path('ff/',GetProvince.as_view(),name='getprovince'),
    path('ll/',GetSubprovince.as_view(),name='province'),
    path('users/',users,name='users'),
    
    path('login/',user_login,name='user_login'),
    path('cre/<int:pk>/',getsubprovince,name='getsubprovince'),
   
    
    path('edit/<int:pk>/',pump_edit,name='pump_edit'),
    path('news_delete/<int:pk>/',pump_delete,name='pump_delete'),
    path('news_del/<int:pk>/',pump_del,name='pump_del'),

    path('logout/',loud,name='logout'),
    path('tuman/',tuman,name='tuman'),
    
    path('',NewsList.as_view(),name='news'),
    path('register/',register,name='register'),
    path('search/',SearchResult.as_view(),name='searchresult'),
   
    path('manitoringvil/',manitoringvil,name='manitoringvil'),
    path('manitoringtuman/',manitoringtuman,name='manitoringtuman'),


    

  


]
