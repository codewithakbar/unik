from django.db import models

from ckeditor.fields import RichTextField

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=211, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    slug = models.SlugField(null=False, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


    def __str__(self):                           
        full_path = [self.name]                 
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])
    

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=224)
    desc = RichTextField(default="12")
    category = models.ManyToManyField(to=Category, related_name='contents')

    image = models.ImageField(upload_to="content/%Y/%m/%d", height_field=None, width_field=None, max_length=None, blank=True, null=True)

    pdf = models.FileField(upload_to='pdfsd/', blank=True, null=True)

    # Fakultet
    nomi = models.CharField(max_length=224, blank=True, null=True, verbose_name="Fakultent Nomi")
    summa = models.DecimalField(max_digits=11,decimal_places=0, default=0, blank=True, null=True, verbose_name="Summasi")

    # Rektor
    rektor_image = models.ImageField(upload_to="rektor/%Y/%m/", blank=True, null=True)
    lavozim = models.CharField(max_length=223, blank=True)
    desc_rek = models.TextField(blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['title']


    def __str__(self) -> str:
        return self.title
    


class Malumotlar(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=224, blank=True)
    desc = RichTextField()

    image = models.ImageField(upload_to="mailumotlar/%Y/%m/%d", height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return self.title
    


class Bannercha(MPTTModel):
    title = models.CharField(max_length=232)
    image = models.ImageField(upload_to='bannercha/', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self) -> str:
        return self.title
    


class Fakultetlar(models.Model):
    # name = models.CharField(max_length=224, blank=True)
    # summa = models.DecimalField(max_digits=11,decimal_places=0,default=0)

    content = models.ForeignKey(to=Content, default=None, related_name='content', on_delete=models.CASCADE)


    def __str__(self):
        return self.content.title
    
    class Meta:
        verbose_name = "Fakultet"
        verbose_name_plural = "Fakultetlar"
        

# Musor 
class Kunduz(models.Model):
    name = models.CharField(max_length=224, blank=True)
    summa = models.DecimalField(max_digits=11,decimal_places=0,default=0)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kunduz"
        verbose_name_plural = "Kunduzgilar"


class Sirtqi(models.Model):
    name = models.CharField(max_length=224, blank=True)
    summa = models.DecimalField(max_digits=11,decimal_places=0,default=0)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Sirtqi"
        verbose_name_plural = "Sirtqilar"


class OqishniKochirish(models.Model):
    
    desc = RichTextField()


    def __str__(self):
        return self.desc[1:7]
    
    class Meta:
        verbose_name = "OqishniKochirish"
        verbose_name_plural = "OqishniKochirishlar"


class Magistr(models.Model):
    name = models.CharField(max_length=224, blank=True)
    summa = models.DecimalField(max_digits=11,decimal_places=0,default=0)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Magistr"
        verbose_name_plural = "Magistrlar"

    
class Talabalar(models.Model):
    name = models.CharField(max_length=224, blank=True)
    summa = models.DecimalField(max_digits=11, decimal_places=0, default=0)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"


class Rektorat(models.Model):
    lavozim = models.CharField(max_length=223, blank=True)
    desc = RichTextField()

    image = models.ImageField(upload_to='rektors/')

    def __str__(self) -> str:
        return self.lavozim


class Book(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

# Images 4 
class Images(models.Model):
    product = models.ForeignKey(Content, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='contents/%Y/%m/%d', blank=True, null=True)


class MalImages(models.Model):
    mal = models.ForeignKey(Malumotlar, default=None, related_name='images', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='malconte/%Y/%m/%d', blank=True, null=True)
