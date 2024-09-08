from django.urls import path
from .import views

from .views import test_404_view

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('test-404/', test_404_view, name='test-404'),
]
