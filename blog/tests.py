from urllib import response
from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog


class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Blog.objects.create(
            title= 'A good title',
            body='Nice body content',
            author=self.user,
            )
            
    def test_string_representation(self):
        blog = Blog(title='A sample title')
        self.assertEqual(str(blog), blog.title)

    def test_blog_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_blog_detail_view(self):
        response = self.client.get('/blog/1/')
        no_response = self.client.get('/blog/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/blog/1/')
    
    def test_blog_create_view(self):
        response = self.client.post(reverse('blog_new'), {
            'title': 'New title',
            'body' : 'New text',
            'author' : self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
    
    def test_blog_update_view(self):
        response = self.client.post(reverse('blog_edit', args='1'), {
            'title' : 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_blog_delete_view(self):
        response = self.client.get(reverse('blog_delete', args='1'))
        self.assertEqual(response.status_code, 200)

    

    


# Create your tests here.
