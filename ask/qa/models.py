from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField('date published', auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects=QuestionManager() 
    
    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('qa:question', args=(self.id,)) #kwargs={'qa_id': self.id})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
