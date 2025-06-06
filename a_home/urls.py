from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('post/detail/<str:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('icon/<str:icon_id>/', views.icon_detail, name='icon'),
    ]