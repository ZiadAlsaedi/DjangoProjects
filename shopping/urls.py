"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from phone import views as v1
from shop import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/<int:id>/',v1.details,name='details'),
    path('auth_login/',v1.auth_login ,name='auth_login'),
    path('showphone/',v1.showphone , name='showphone'),
    path('auth_register/',v1.auth_register ,name='auth_register'),
    path('auth_logout/',v1.auth_logout ,name='auth_logout'),
    path('checkout/',v1.checkout ,name='checkout'),
    path('add_to_cart/<int:id>/',v1.add_to_cart ,name='add_to_cart'),
    path('showitem/',v2.showitem , name='showitem'),
     path('s_details/<int:id>/',v2.s_details,name='s_details'),
    path('s_auth_login/',v2.auth_login ,name='auth_login'),
    path('s_auth_register/',v2.auth_register ,name='auth_register'),
    path('s_auth_logout/',v2.auth_logout ,name='auth_logout'),
    path('s_checkout/<int:id>/',v2.s_checkout ,name='s_checkout'),
    path('s_add_to_cart/<int:id>/',v2.s_add_to_cart ,name='s_add_to_cart'),
    path('',v2.indexs , name='indexs'),
    path('showitemhome/',v2.showitemhome , name='showitemhome'),
    path('showitemelectric/',v2.showitemelectric , name='showitemelectric'),
    path('showitemeclaner/',v2.showitemeclaner , name='showitemeclaner'),
    path('allitem/',v2.allitem , name='allitem'),
    path('Buys/',v2.Buys , name='Buys'),






    
]
