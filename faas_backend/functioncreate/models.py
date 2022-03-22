from django.db import models
from django.utils import timezone


class FunctionFile(models.Model):
    content = models.FileField(upload_to="upload/%Y%m%d/")


class FunctionCreate(models.Model):
    title = models.CharField(max_length=100)

    cluster = models.CharField(max_length=100)

    data_store = models.CharField(max_length=100)

    log_store = models.CharField(max_length=100)

    file = models.ForeignKey(
        FunctionFile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )

    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

