from django.db import models

import datetime


class SkillForgeBaseQuerySet(models.QuerySet):
    def update(self, *args, **kwargs):
        if 'last_updated' not in kwargs:
            kwargs['last_updated'] = datetime.datetime.now()
        return super().update(**kwargs)

class BaseModel(models.Model):
    pass