from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('search_customer/', views.search_customer, name='search_customer'),
    path('show_name/', views.show_name, name='show_name'),
]
