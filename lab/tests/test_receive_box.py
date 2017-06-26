import datetime

from django.test import TestCase, tag
from django.utils import timezone

from ..models import Box, BoxType, Manifest
from ..receive import ReceiveBox
from ..receive import BoxRejectedException, DuplicateBoxException


class TestReceiveBox(TestCase):

    @tag('check_box_items')
    def test_check_box_items(self):
        """
        Asserts that the items in a box is the same in the manifest
        """
        boxtype = BoxType.objects.create(
            name='Bluffy Coat', down=10, across=10, total=100)
        box = Box.objects.create(
            box_identifier='2831-9900-8872',
            category='storage',
            box_type=boxtype)
        box.boxitem_set.create(position=1)
        box.boxitem_set.create(position=2)
        manifest = Manifest.objects.create()
        manifest.manifestitem_set.create(identifier='3336-2332-6612')
        manifest.manifestitem_set.create(identifier='9936-8373-0000')
        ReceiveBox(box=box, manifest=manifest)
        self.assertEqual(box.count(), manifest.count())

    @tag('receive_valid_box')
    def test_receive_valid_box(self):
        """
        Asserts whether a box is valid.
        """
        boxtype = BoxType.objects.create(
            name='Whole Blood',
            across=9,
            down=9,
            total=81)
        box = Box.objects.create(
            box_identifier='2831-9900-8872',
            category='storage',
            box_type=boxtype
        )
        box.boxitem_set.create(position=1)
        manifest = Manifest.objects.create()
        ReceiveBox(box=box, manifest=manifest)

    @tag('accept_valid_box')
    def test_accept_valid_box(self):
        """
        Accepts a valid box.
        """
        boxtype = BoxType.objects.create(
            name='Whole Blood', across=10, down=10, total=100
        )
        box = Box.objects.create(
            box_identifier='2809-9900-8872',
            category='storage',
            box_type=boxtype,
            box_datetime=timezone.now() - datetime.timedelta(days=5)
        )
        box.boxitem_set.create(position=1)
        manifest = Manifest.objects.create(
            manifest_datetime=timezone.now() - datetime.timedelta(days=5))
        manifest.manifestitem_set.create(
            identifier='3309-2332-6612'
        )
        ReceiveBox(box=box, manifest=manifest)
        self.assertTrue(box.accept_box)

    @tag('receive_invalid_box')
    def test_receive_invalid_box(self):
        """
        Asserts whether a box is invalid.
        """
        boxtype = BoxType.objects.create(
            name='Bluffy Coat', across=9, down=9, total=81)
        box = Box.objects.create(
            box_identifier='2831-9900-8872',
            category='storage',
            box_type=boxtype
        )
        self.assertRaises(
            BoxRejectedException,
            ReceiveBox,
            box=box
        )

    @tag('check_time_equal')
    def test_check_time_equal(self):
        """
        Asserts that the box and manifest datetime are equal.
        """
        boxtype = BoxType.objects.create(
            name='Bluffy Coat', down=10, across=10, total=100)
        box = Box(
            box_identifier='2831-9900-8872',
            category='storage',
            box_type=boxtype,
            box_datetime=timezone.now(),
        )
        manifest = Manifest(
            manifest_identifier='2001-9900-8872',
            manifest_datetime=timezone.now(),
        )
        is_date = ReceiveBox(box=box,
                             manifest=manifest).is_box_datetime_valid()
        self.assertTrue(is_date)

    @tag('manifest_time')
    def test_check_manifest_greater_than_boxtime(self):
        """
        Asserts that a manifest datetime should be greater than\
        the box datetime.
        """
        boxtype = BoxType.objects.create(
            name='Bluffy Coat', down=10, across=10, total=100)
        box = Box(
            box_identifier='2831-9900-8872',
            category='storage',
            box_type=boxtype,
            box_datetime=timezone.now() - datetime.timedelta(days=10),
        )
        manifest = Manifest(
            manifest_identifier='2001-9900-8872',
            manifest_datetime=timezone.now() - datetime.timedelta(days=5),
        )
        is_date = ReceiveBox(box=box,
                             manifest=manifest).is_box_datetime_valid()
        self.assertTrue(is_date)

    @tag('manifest_time_not_equal')
    def test_check_manifest_datetime_not_equal(self):
        """
        Asserts that the box datetime can't be in the future.
        """
        box = Box(
            box_identifier='2831-9900-8872',
            category='storage',
            box_datetime=timezone.now() + datetime.timedelta(days=5),
        )
        manifest = Manifest(
            manifest_identifier='2001-9900-8872',
            manifest_datetime=timezone.now() - datetime.timedelta(days=5),
        )
        is_date = ReceiveBox(box=box,
                             manifest=manifest).is_box_datetime_valid()
        self.assertFalse(is_date)

    @tag('manifest_time_future')
    def test_check_manifest_datetime_isfuture(self):
        """
        Asserts that the manifest datetime can't be in the future.
        """
        box = Box(
            box_identifier='2831-9900-8872',
            category='storage',
            box_datetime=timezone.now() + datetime.timedelta(days=5),
        )
        manifest = Manifest(
            manifest_identifier='2001-9900-8872',
            manifest_datetime=timezone.now() + datetime.timedelta(days=10),
        )
        is_date = ReceiveBox(
            box=box,
            manifest=manifest
        ).is_box_datetime_valid()
        self.assertFalse(is_date)

    @tag('duplicateBox')
    def test_received_duplicate_box(self):
        """
        Asserts if a box already exists in the database
        """
        boxtype = BoxType.objects.create(
            name='Bluffy coat', across=9, down=5, total=45)
        box = Box.objects.create(
            box_identifier='2831-9900-8872',
            category='storage',
            box_type=boxtype)
        manifest = Manifest.objects.create()
        ReceiveBox(box=box, manifest=manifest)
        self.assertTrue(box.accept_box)
        self.assertRaises(
            DuplicateBoxException,
            ReceiveBox,
            box=box,
            manifest=manifest)
