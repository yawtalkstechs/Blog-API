from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        dan = User.objects.create_user(username='dan', password='dan123')
        dan.save()

        testpost = Post.objects.create(author=dan, title='Blog Title', body='My content')
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'dan')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'My content')