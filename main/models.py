from django.db import models
from django.utils.safestring import mark_safe

# Banner
class Banner(models.Model):
    img=models.CharField(max_length=200)
    alt_text=models.CharField(max_length=300)

# Create your models here.
# Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.ImageField(upload_to='cat_imgs/')

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100)
    description = models.ImageField(upload_to='brand_imgs/')

    def __str__(self):
        return self.title

# Color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    # class Meta:
    #     verbose_name_plural='4. Colors'
    #
    # def color_bg(self):
    #     return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_imgs/')
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    price = models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color =models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size, on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.title