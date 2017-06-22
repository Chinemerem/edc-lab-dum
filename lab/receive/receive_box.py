from lab.models.box import Box


class DamagedBoxRejected(Exception):
    pass


class ReceiveBox:

    def __init_(self, box=None):
        self.box = box if box.status is not 'damaged' else None
        if not self.box:
            raise DamagedBoxRejected(
                f'The box is rejected because it is not in good condition'
                f'Box status is {box.status}')

    def is_box_valid(self):
        return isinstance(self.box, Box)

#     def isAllItemsTypeValid(self):
#         items = self.box.boxitem_set.all()
