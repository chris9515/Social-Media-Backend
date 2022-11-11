from django.test import TestCase

from api import models


class ModelTest(TestCase):
    user = models.User.objects.get(username='admin')
    post = models.Post.objects.create(
        title="Testing title",
        description="Testing a sample description",
        user=user
    )

    def test_post_model_str(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_model_user(self):
        self.assertEqual(self.post.user, self.user)

    def test_post_model_delete(self):
        count_before = models.Post.objects.count()
        self.post.delete()
        count_after = models.Post.objects.count()
        self.assertEqual(count_before, count_after)

