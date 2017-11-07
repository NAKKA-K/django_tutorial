from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import resolve_url
from unittest import mock
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

class ViewTest(TestCase):
    def test_index(self):
        response = self.client.get(resolve_url('polls:index')) # 指定URLへアクセス
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.context['questions'].count()) # テスト時のDBは毎回初期状態から始まる

        # 新規データを作成
        Question.objects.create(
            question_text = "aaa",
            published_date = timezone.now(),
        )
        response = self.client.get(resolve_url('polls:index')) # 新しいデータを登録したため、ページを更新後テスト
        self.assertEqual(1, response.context['questions'].count())
        self.assertEqual('aaa', response.context['questions'].first().question_text)
