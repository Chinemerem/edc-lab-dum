from ..model_mixins import AliquotModelMixin
from ..model_mixins  import AliquotIdentifierModelMixin
from ..identifiers import AliquotIdentifier

from django.db import models


class Aliquot(AliquotModelMixin, AliquotIdentifierModelMixin):
    objects = models.Manager()
    