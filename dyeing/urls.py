"""dyeing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from billing.views import signin,signup,dashboard,signout,material,create_list,create_details,bill,generate
urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", signup),
    path("signin/", signin),
    path('dashboard/',dashboard),
    path('signout/',signout),
    path('material/',material),
    path('create_list/',create_list),
    path('create_details/',create_details),
    path('bill/', bill),
    path('generate/<int:numb>/',generate),
    
]
