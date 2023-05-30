from django.db import models

from ckeditor.fields import RichTextField


class Banner(models.Model):
    title = models.CharField(max_length=233)
    image = models.ImageField(upload_to="banners/", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=211, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    slug = models.SlugField(null=False, unique=True)

    # class Meta:
    #     related_name = "Kategoriya"
    #     related_plural_name = "Kategoriyalar"

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])
    

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=224, blank=True)
    desc = RichTextField()
    category = models.ForeignKey(to=Category, null=True, blank=True, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="content/%Y/%m/%d", height_field=None, width_field=None, max_length=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Malumotlar(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=224, blank=True)
    desc = RichTextField()

    image = models.ImageField(upload_to="mailumotlar/%Y/%m/%d", height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return self.title
    

class Fakultetlar(models.Model):
    name = models.CharField(max_length=224, blank=True)
    summa = models.DecimalField(max_digits=11,decimal_places=0,default=0)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fakultet"
        verbose_name_plural = "Fakultetlar"
        

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