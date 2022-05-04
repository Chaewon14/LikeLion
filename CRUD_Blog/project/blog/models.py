from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    contents = models.TextField(default='empty')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=10, default='me')
    category = models.CharField(max_length=10, default='all')

    def __str__(self):
        return self.title

    def summary(self):
        summary = self.contents[:120] + "ꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏꞏ"
        return summary