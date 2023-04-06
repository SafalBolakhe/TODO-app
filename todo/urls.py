from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.todo),
    path('create/', views.createtodo, name = 'create'),
    path('delete/<int:i>/', views.removetodo, name = 'remove'),
]