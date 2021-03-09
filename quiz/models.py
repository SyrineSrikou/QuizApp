from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="images", blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    option5 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)