import uuid
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

from ckeditor.fields import RichTextField

import datetime


class SkillForgeBaseQuerySet(models.QuerySet):
    def update(self, *args, **kwargs):
        if "last_updated" not in kwargs:
            kwargs["last_updated"] = datetime.datetime.now()
        return super().update(**kwargs)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseCategory(BaseModel):
    title = models.CharField(max_length=127)
    slug = models.SlugField(max_length=255, allow_unicode=True)
    view = models.PositiveIntegerField(default=0)
    code = models.CharField(unique=True, max_length=9, null=True, blank=True)

    class Meta:
        abstract = True


class BaseComment(BaseModel):
    content = RichTextField(blank=False, null=False)
    view = models.PositiveIntegerField(default=0)
    like = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class BaseTag(BaseModel):
    title = models.CharField(max_length=127, unique=True)
    slug = models.SlugField(max_length=255, allow_unicode=True)
    view = models.PositiveIntegerField(default=0)
    like = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class BasePost(BaseModel):
    code = models.CharField(unique=True, max_length=32, default=get_random_string(length=32))
    title = models.CharField(max_length=127, null=False, blank=False)
    slug = models.SlugField(unique=True, max_length=255, allow_unicode=True)
    content = RichTextField(null=False, blank=False)
    view = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True