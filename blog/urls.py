from django.urls import path
from .views import BlogHomeView, BlogDetailView, BlogCreteView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/',BlogDeleteView.as_view(), name='blog_delete' ),
    path('blog/new/', BlogCreteView.as_view(), name='blog_new'),
]