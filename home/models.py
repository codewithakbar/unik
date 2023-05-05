from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=233)
    image = models.ImageField(upload_to="banner/%Y/%m/%d", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

    
