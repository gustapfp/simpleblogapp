from .models import Blog
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogHomeView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs_list'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'