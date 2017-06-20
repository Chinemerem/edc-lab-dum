from lab.model_mixins.aliquot.aliquot_model_mixin import AliquotModelMixin
from django.db import models


class Aliquot(AliquotModelMixin):
    objects = models.Manager()
    