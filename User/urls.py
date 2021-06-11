from django.conf.urls import url
from . import views
from django.urls import path, include
from User.views import Registerapi
urlpatterns = [
      path('Register/', Registerapi),
   
      path('Login/', views.Login.as_view(), name="api_auth"),

]
