from django.db import models

from ...model_mixins import ManifestModelMixin


class Manifest(ManifestModelMixin):

    objects = models.Manager()

    manifest_on_database = models.BooleanField(
        default=False,
        help_text='Flagged if electronic '
        'manifest exists')

    def __str__(self):
        return '{} created on {} by {}'.format(
            self.manifest_identifier,
            self.manifest_datetime.strftime('%Y-%m-%d'),
            self.user_created)

    def count(self):
        return self.manifestitem_set.all().count()

    class Meta(ManifestModelMixin.Meta):
        app_label = 'lab'
