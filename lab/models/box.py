from django.db import models
from django.utils import timezone
from django.db.models import PROTECT
from ..constants import TESTING, STORAGE, DAMAGED, OTHER, OPEN
from .box_type import BoxType


BOX_CATEGORY = (
    (TESTING, 'Testing'),
    (STORAGE, 'Storage'),
    (OTHER, 'Other'),
)

STATUS = (
    (OPEN, 'Open'),
    (DAMAGED, 'Damaged'),
)


class Box(models.Model):

    box_identifier = models.CharField(
        max_length=25,
        editable=False,
        unique=True)

    name = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    box_type = models.ForeignKey(
        BoxType, on_delete=PROTECT)

    box_datetime = models.DateTimeField(
        default=timezone.now)

    category = models.CharField(
        max_length=25,
        default=TESTING,
        choices=BOX_CATEGORY)

    status = models.CharField(
        max_length=15,
        default=OPEN,
        choices=STATUS)

    accept_box = models.BooleanField(
        default=False,
        help_text='Tick to accept/decline this box')

    comment = models.TextField(
        null=True,
        blank=True)

    objects = models.Manager()
