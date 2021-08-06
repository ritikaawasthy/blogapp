from django.urls import path
from . import views



urlpatterns = [
path('login/', views.loginView, name ='login'),
path('signup/', views.signUpView, name ='signup'),
path('', views.home, name ='home'),
path('logout/', views.logoutView, name ='logout'),
path('addblog/', views.addBlog, name ='addblog'),

]
