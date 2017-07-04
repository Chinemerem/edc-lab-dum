from django.db import models
from django.utils import timezone


class Receive(models.Model):

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
    clinician_initials = models.CharField(
        verbose_name='Clinicians\'s initials',
        max_length=3,)

    tube_count = models.IntegerField(default=1, null=True, blank=False)

    def __str__(self):
        return '{}: {}'.format(
            self.receive_identifier,
            self.receive_datetime.strftime('%Y-%m-%d %H:%M'))
