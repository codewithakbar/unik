from django.db import models

# Create your models here.

class Yangiliklar(models.Model):
    title = models.CharField(max_length=232)
    desc = models.TextField()
    image = models.ImageField(default="news/%Y/%m/%d", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



