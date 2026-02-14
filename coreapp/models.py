from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Categories(models.Model):
    catName = models.CharField(max_length=150)

    def __str__(self):
        return  self.catName