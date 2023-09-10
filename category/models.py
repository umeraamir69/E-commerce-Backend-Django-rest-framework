from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 255 ,help_text = "Category Name")
    slug = models.SlugField(unique = True ,max_length=10 , help_text="Category Code (Max-6 digits)  ABC-123" , blank =  False )
    description = models.TextField()
    is_active = models.BooleanField(default = True)
    is_featured = models.BooleanField(default = False)
    image = models.ImageField(upload_to='category_images/', blank = False)

    def __str__(self):
        return f"{self.name} {self.slug}"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['name' ,'slug' ]
        db_table = 'category'    
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def save(self, *args, **kwargs):
        if self.image:
            extension = self.image.name.split('.')[-1]  # Get the file extension
            self.image.name = f"{self.slug}.{extension}"

        super().save(*args, **kwargs)