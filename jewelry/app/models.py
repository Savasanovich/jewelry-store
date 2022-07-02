from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Product(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img')
    created_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.name
