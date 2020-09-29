from django.db import models

# Create your models here.
class Question(models.Model):
    ct_name = models.CharField(max_length=300)
    question = models.CharField(max_length=600)
    solution = models.CharField(max_length=600)
    def __str__(self):
        return self.ct_name