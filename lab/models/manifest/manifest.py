from django.db import models
from django.db.models import PROTECT

from .consignee import Consignee
from .shipper import Shipper
from ...model_mixins import ManifestModelMixin


class Manifest(ManifestModelMixin):

    consignee = models.ForeignKey(
        Consignee,
        verbose_name='Consignee',
        on_delete=PROTECT)

    shipper = models.ForeignKey(
        Shipper,
        verbose_name='Shipper/Exporter',
        on_delete=PROTECT)

    objects = models.Manager()

    def __str__(self):
        return '{} created on {} by {}'.format(
            self.manifest_identifier,
            self.manifest_datetime.strftime('%Y-%m-%d'),
            self.user_created)

    @property
    def count(self):
        return self.manifestitem_set.all().count()

    class Meta(ManifestModelMixin.Meta):
        app_label = 'lab'
