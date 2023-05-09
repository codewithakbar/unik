from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=233)
    image = models.ImageField(upload_to="banners/", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

    
class Category(models.Model):
    name = models.CharField(max_length=211, blank=True)

    class Meta:
        related_name = "Kategoriya"
        related_plural_name = "Kategoriyalar"

    def __str__(self) -> str:
        return self.name

