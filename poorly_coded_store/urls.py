from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_item/', views.process_checkout),
    path('checkout/', views.checkout)
]
