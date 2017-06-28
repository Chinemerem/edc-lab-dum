from django.db import models
from django.utils import timezone


class Receive(models.Model):

    aliqout = models.CharField(
        max_length=50,
        editable=False,
        unique=True
    )

    receive_identifier = models.CharField(
        max_length=25,
        editable=False,
        unique=True
    )

    receive_datetime = models.DateTimeField(
        default=timezone.now
    )
    specimen_type = models.CharField(
        max_length=2
    )

    specimen_condition = models.CharField(
        max_length=2,
        null=True,
        blank=True,
    )

    specimen_reference = models.CharField(
        max_length=25,
        help_text='A unique reference for this patient\'s specimen',
        null=True,
        blank=True
    )

    protocol_number = models.CharField(
        verbose_name='Protocol',
        max_length=15,
        null=True,
        blank=True
    )

    site_code = models.CharField(
        max_length=2,
        null=True,
        blank=True,
    )

    collection_datetime = models.DateTimeField()


class Meta:
    abstract = True
