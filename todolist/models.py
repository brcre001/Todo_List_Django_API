from django.db import models

# Create your models here.

class Todo(models.Model):
    label = models.CharField(max_length=300)
    done = models.BooleanField()

    def __str__(self):
        return self.text