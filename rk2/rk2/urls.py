"""rk2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('browser/', include([
        path('', views.read_browser, name='read_browser'),
        path('create/', views.create_browser, name="create_browser"),
        path('update/<int:browser_id>/', views.update_browser, name="update_browser"),
        path('delete/<int:browser_id>/', views.delete_browser, name="delete_browser"),
    ])),
    path('comp_browser/', include([
        path('', views.read_comp_browser, name='read_comp_browser'),
        path('create/', views.create_comp_browser, name="create_comp_browser"),
        path('update/<int:comp_browser_id>/',
             views.update_comp_browser, name="update_comp_browser"),
        path('delete/<int:comp_browser_id>/',
             views.delete_comp_browser, name="delete_comp_browser"),
    ])),
    path('report/', views.report, name="report"),
]
