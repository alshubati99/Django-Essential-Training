from django.urls import path
from . import views

urlpatterns = [
    # if you make home empty '' the default page will be the home page. 
    path('home', views.HomeView.as_view(), name='home'),
    path('authorized',views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='login'
         ),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name = 'signup'
          ),

]