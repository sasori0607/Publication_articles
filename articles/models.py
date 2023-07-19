from django.db import models
from django.utils.timezone import now


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.title
