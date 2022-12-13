from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),    
    path('logout/', views.logout, name='logout'),        
    path('dashboard/', views.dashboard, name='dashboard'),        
    path('essays/<int:essay_id>', views.essay_detail, name='essay_detail'),

]
