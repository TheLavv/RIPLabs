from django.contrib import admin
from django.urls import path

from lab4_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_parrots),
    path('parrot/<int:id>/', views.get_parrot_info)
]
