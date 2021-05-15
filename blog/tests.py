from django.test import TestCase
from . models import Post
from django.contrib.auth.models import User


class ModelTesting(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()
        self.blog = Post.objects.create(title='django', author=test_user1, content = "This is for testing")

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')