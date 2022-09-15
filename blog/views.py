from .models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BlogHomeView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs_list'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreteView(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = '__all__' #  all fields with '__all__' since we only have two: title and author.

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')


