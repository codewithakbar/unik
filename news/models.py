from django.db import models

from ckeditor.fields import RichTextField



class NewsCartegory(models.Model):
    name = models.CharField(max_length=211, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    slug = models.SlugField(null=False, unique=True)

    # class Meta:
    #     related_name = "Kategoriya"
    #     related_plural_name = "Kategoriyalar"

    def __str__(self) -> str:
        return self.name
    

class Yangiliklar(models.Model):
    title = models.CharField(max_length=232)
    desc = RichTextField()
    image = models.ImageField(default="news/%Y/%m/%d", null=True, blank=True)
    category = models.ForeignKey(to=NewsCartegory, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title





