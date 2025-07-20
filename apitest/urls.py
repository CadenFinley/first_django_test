from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.get_item, name='user'),
    path('user/create', views.post_item, name='create_user'),
]