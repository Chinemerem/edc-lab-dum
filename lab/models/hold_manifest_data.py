from django.db import models


class ManifestData(models.Model):
    identifier = models.CharField(
        max_length=25,
        unique=True
    )
    objects = models.Manager()

    def __str__(self):
        return self.identifier


class AliquotData(models.Model):

    identifier = models.CharField(
        max_length=25,
        unique=True
    )
    objects = models.Manager()

    def __str__(self):
        return self.identifier
