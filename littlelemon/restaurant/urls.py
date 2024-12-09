from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>/', views.display_menu_item, name="display_menu_item"),
    path('menu-search/', views.display, name="display"),  
    path('bookings/', views.bookings, name='bookings'), 
]