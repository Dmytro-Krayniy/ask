from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        qts = super().get_queryset().order_by('-added_at')
        return qts

    def popular(self):
        return super().get_queryset().order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes_set')
    # questions = QuestionManager()
    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_url(self):
        return '/question/' + str(self.id)


class Answer(models.Model):
    text = models.TextField(null=False)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)
