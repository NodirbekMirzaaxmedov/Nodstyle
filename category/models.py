from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc = models.TextField(blank=True,null=True)
    category_image = models.ImageField(upload_to='image/category/')

    class Meta:
        verbose_name_plural = 'kategory'
    def __str__(self):
        return self.category_name