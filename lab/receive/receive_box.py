from lab.models.box import Box
from django.utils import timezone


class DamagedBoxRejected(Exception):
    pass


class ReceiveBox:

    def __init__(self, box=None, manifest=None):
        self.box = box
        self.manifest = manifest
        if not self.box:
            raise DamagedBoxRejected(
                f'The box is rejected because it is not in good condition'
                f'Box status is {box.status}')

    def is_box_valid(self):
        return isinstance(self.box, Box)

    def is_box_datetime_valid(self):
        now = timezone.now()
        dateCheck = False
        if self.manifest.manifest_datetime <= now:
            if self.box.box_datetime <= self.manifest.manifest_datetime:
                dateCheck = True

        return dateCheck

#     def isAllItemsTypeValid(self):
#         items = self.box.boxitem_set.all()
