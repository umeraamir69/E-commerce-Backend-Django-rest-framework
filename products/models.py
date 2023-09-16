from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from category.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=10 , help_text= "three digits with three numbers (AAA-000)")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    # one-to-one relationship between products and categories
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    # for manament purposes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Add other fields specific to your product
    # For example, you might want to add fields like brand, category, etc.

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate a slug from the product name
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])




class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    # Add other fields specific to your image, such as a caption or description

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


    def formatted_description(self):
        # Get the index of the current image in the related prodsuct's images
        index = list(self.product.images.all()).index(self) + 1
        return f"{index} # {self.product.slug} "

    def __str__(self):
        return self.formatted_description()
