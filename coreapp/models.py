import os.path
import os
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import  ValidationError

User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def validate_image_size(image):
        if image.size > 5 * 1024 *1024:
            raise  ValidationError("Image is too large ( > 5MB )")

    image = models.ImageField(upload_to='post_images/', blank=True, null=True, validators=[validate_image_size])

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Blog.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)
            except Blog.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        super().delete(*args, **kwargs)



class Categories(models.Model):
    catName = models.CharField(max_length=150)

    def __str__(self):
        return  self.catName