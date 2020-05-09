from django.contrib import admin
from .models import Forum, Comment, Category, SubCategory

from tinymce.widgets import TinyMCE
from django.db import models

class ForumAdmin(admin.ModelAdmin):
    # fields = ["title",
    #           "user",
    #           "desc"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Forum, ForumAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(SubCategory)
