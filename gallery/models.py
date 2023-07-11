from django.db import models


class TopBanner(models.Model):
    name = models.CharField(max_length=33)
    image = models.ImageField(upload_to="gallery/%Y/%m%d")

    def __str__(self) -> str:
        return self.name



class GalleryImages(models.Model):
    name = models.CharField(max_length=33)
    image = models.ImageField(upload_to="gallery/%Y/%m%d")

    def __str__(self) -> str:
        return self.name


class VideoGallery(models.Model):
    name = models.CharField(max_length=33)
    video = models.FileField(upload_to="gallery/video/%Y/%m%/%d")
    thumnail = models.ImageField(upload_to="thumnail/")


    def __str__(self) -> str:
        return self.name

