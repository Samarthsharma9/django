from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    
    path('admin/',admin.site.urls),
    
    path('',views.home, name='home'),
    
    path('Login/login.html',views.Login,name='login'),
    
    path('Login/login.html',views.Login,name='Create_account'),
    
    path('Contractor/index.html',views.Contractor,name='Contractor'),
    
    path('Home Design Plan/index.html',views.Home_Design_Plan,name='Home Design Plan'),
    
    path('Construction Material/index.html',views.Construction_Material,name='Construction Material'),
    
    path('Architect/index.html',views.Architect,name='Architect'),
    
    path('Interior Design/index.html',views.Interior_Design,name='Interior Design'),
    
    path('Precast Material/index.html',views.Precast_Material,name='Precast Material'),
    
    path('Interior Designer/index.html',views.Interior_Designer,name='Interior Designer')
    
      
]