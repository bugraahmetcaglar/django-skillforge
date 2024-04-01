from django.db import models

import datetime


class SkillForgeBaseQuerySet(models.QuerySet):
    def update(self, *args, **kwargs):
        if "last_updated" not in kwargs:
            kwargs["last_updated"] = datetime.datetime.now()
        return super().update(**kwargs)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    created_by = models.ForeignKey(null=True, on_deleted=models.SET_NULL, related_name="created_by_+")
    updated_by = models.ForeignKey(null=True, on_deleted=models.SET_NULL, related_name="updated_by_+")
