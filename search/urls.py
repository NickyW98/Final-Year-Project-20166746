from django.urls import path
from django.contrib import admin
from search import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.SearchPage, name='search_result'),
    path('', views.HomePage, name='home'),
    path('', views.webpage1, name='webpage1'),
    path('test', views.test, name='test')
]