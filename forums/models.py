from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    def __str__(self):
        return self.category

    category = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)

class SubCategory(models.Model):
    def __str__(self):
        return self.subcategory
    subcategory = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, blank = True, null = True, on_delete = models.CASCADE)
    desc = models.CharField(max_length = 200)
    slug = models.SlugField(null = True, blank=True)

    #def get_absolute_url(self):
    #    return reverse('list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.subcategory, allow_unicode=True)
        super(SubCategory, self).save(*args, **kwargs)

class Forum(models.Model):
    def __str__(self):
        return self.title

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, blank = True, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    def __str__(self):
        return self.desc

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
