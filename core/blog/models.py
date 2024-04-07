import uuid

from django.db import models

from skillforge.models import BaseModel, BaseCategory, BasePost, BaseComment
from skillforge.utils import NullableCharField
from ckeditor.fields import RichTextField


class BlogCategory(BaseCategory):
    pass


class Blog(BasePost):
    # media = models.FileField(null=True, blank=True, storage=ArticleMediaStorage(), default="no-image-available.png")
    category = models.ForeignKey(
        BlogCategory, related_name="blog_categories", on_delete=models.SET_NULL, blank=False, null=True
    )
    introduction = models.NullableCharField(max_length=1000)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ArticleComment(BaseComment):
    article = models.ForeignKey(
        Blog, related_name="blog_comments", on_delete=models.DO_NOTHING, null=False, blank=False
    )

    class Meta:
        ordering = ["-created_at"]
