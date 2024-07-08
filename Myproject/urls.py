"""
URL configuration for Myproject project.

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
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# from home.views import home, about, contact
from receipe_pro.views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/',admin.site.urls),
    # path('Recipes/',Recipes,name ="Recipes"),
    path('main/',main,name ="main"),
    path('Login/', Login_page, name="Login"),
    path('Logout/', Logout_page, name="Logout_page"),
    path('',main,name="main"),
    path('register/',Reg, name="reg"),
    path('tandc/',tandc,name="tandc"),
    path('about/',about,name="about"),
    path('addrecipe/',addrecipe,name="addrecipe"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('about1/',about1,name="about1"),

    path('Recipe_detail/<int:pk>/',Recipe_detail,name="Recipe_detail"),
    path('delete/<int:pk>/',delete,name="delete")
    

    

    # path('Success-page/',Success_page,name="Success_page"),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

