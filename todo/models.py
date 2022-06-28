from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class TODOS(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)
    is_finished = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title