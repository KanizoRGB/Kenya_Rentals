"""
URL configuration for Kenya_rentals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rentalsapp import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about,name='about'),
    path('agents/', views.agents, name='agents'),
    path('services/', views.services, name='services'),
    path('properties/', views.properties, name='properties'),
    path('starter/', views.starter, name='starter'),
    path('contact/', views.contact, name='contact'),
    path('agentregister/', views.agentregister, name='agentregister'),
    path('agents/', views.agents, name='agents'),
    path('agentlogin/', views.agentlogin, name='agentlogin'),
    path('houseuploads/', views.houseuploads, name='houseuploads'),
    path('showproperties/', views.showproperties, name='showproperties'),
    path('housedelete/<int:id>', views.housedelete, name='housedelete'),
    path('houseedit/<int:id>', views.houseedit, name='houseedit'),
    path('houseupdate/<int:id>', views.houseupdate, name='houseupdate'),
    path('propertysingle/', views.propertysingle, name='propertysingle'),
    path('searchhouse/', views.searchhouse, name='searchhouse'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
]
