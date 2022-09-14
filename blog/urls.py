from django.urls import path
from .views import BlogHomeView, BlogDetailView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]