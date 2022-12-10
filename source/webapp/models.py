from django.db import models
from django.urls import reverse

class Poll(models.Model):
    question = models.CharField(max_length=100, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def get_success_url(self):
        return reverse('index', kwargs={'pk': self.pk})
    def __str__(self):
        return f'{self.pk}. {self.question}'
# Create your models here.
class Choice(models.Model):
    variation = models.CharField(max_length=500, verbose_name='Текст Варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return f'{self.pk}. {self.variation}'