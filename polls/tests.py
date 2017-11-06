from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Question

# Create your tests here.
class PollTest(TestCase):
    def test_was_published_recently(self):
        obj = Question(published_date = timezone.now() - timedelta(days = 1, minutes = 1))
        self.assertFalse(obj.was_published_recently(), '1日と1分前に公開')

        obj = Question(published_date = timezone.now() - timedelta(days = 1) + timedelta(minutes = 1))
        self.assertTrue(obj.was_published_recently(), '1日と1分後に公開')

        obj = Question(published_date = timezone.now() - timedelta(minutes = 1))
        self.assertTrue(obj.was_published_recently(), '1分前に公開')

        obj = Question(published_date = timezone.now() + timedelta(minutes = 1))
        self.assertFalse(obj.was_published_recently(), '1分後に公開')