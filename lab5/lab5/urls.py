from django.contrib import admin
from django.urls import path

from lab5_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_comp_browsers_list),
    path('computer/<int:id>/', views.get_computer, name='computer_url'),
    path('browser/<int:id>/', views.get_browser, name='browser_url')
]
