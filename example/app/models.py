from django.db import models
from django.contrib.postgres.fields import JSONField


class JSONModel(models.Model):
    data = JSONField(default={})


class ArrayJSONModel(models.Model):
    roles = JSONField(default=[])


class Tag(models.Model):
    name = models.CharField('name', max_length=10)
