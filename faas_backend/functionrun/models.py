from django.db import models
from django.utils import timezone


class RunPath(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']