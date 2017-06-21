from django.db import models
from django.utils import timezone

from ..constants import PACKED,SHIPPED,\
VERIFIED,TESTING,STORAGE



OTHER = 'other'
OPEN = 'open'
# WHOLE_BLOOD = '02'



BOX_CATEGORY = (
    (TESTING, 'Testing'),
    (STORAGE, 'Storage'),
    (OTHER, 'Other'),
)

STATUS = (
    (OPEN, 'Open'),
    (VERIFIED, 'Verified'),
    (PACKED, 'Packed'),
    (SHIPPED, 'Shipped'),
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

    accept_primary = models.BooleanField(
        default=False,
        help_text='Tick to allow \'primary\' specimens to be added to this box')

    comment = models.TextField(
        null=True,
        blank=True)

