from django.test import TestCase, tag
from django.utils import timezone
from ..models import Aliquot, Box, BoxType, Manifest, ManifestItem
from ..models import ManifestData, AliquotData
# from edc_new_app.model_mixins import aliquot
# from edc_new_app.models import manifest_holding_table, Manifest, ManifestItem
from ..receive import ReceiveAliquot


class TestReceive(TestCase):

    def setUp(self):
        self.manifest = Manifest.objects.create(
            manifest_identifier='M02ABCDQWERT')
        self.manifest_item = ManifestItem.objects.create(
            manifest=self.manifest,
            identifier='AAAO-QWER-2RRR')
        self.aliquot = Aliquot(
            aliquot_identifier='AAAA-EDDD-AAAA',
            aliquot_datetime=timezone.now(),
            condition='10',
        )
        boxtype = BoxType.objects.create(
            name='Buffy Coat', across=10, down=10, total=100)

        box = Box.objects.create(
            box_identifier='AAAO-QWER-2RRR',
            category='testing',
            box_type=boxtype
        )
        box.boxitem_set.create(identifier='AAAA-EDDD-AAAA',
                               position=1)
        box.save()

    @tag('1')
    def test_aliqout_in_manifest_contents(self):
        ManifestData.objects.create(
            identifier='AAAAA-AAAA')
        a = AliquotData.objects.create(
            identifier='AAAAA-AAAA')
        ManifestData.objects.create(
            identifier='AAAAA-BBBB')
        ManifestData.objects.create(
            identifier='FFPOE-AALL')
        self.assertEqual(a.identifier,
                         str(ManifestData.objects.all().get(
                             identifier__exact=a.identifier
                         )))

    @tag('2')
    def test_alliquot_list_equal_manifest_list(self):
        AliquotData.objects.create(
            identifier='AAAAA-AAAA')
        ManifestData.objects.create(
            identifier='AAAAA-AAAA')
        self.assertEqual(AliquotData.objects.count(),
                         ManifestData.objects.count())

    @tag('3')
    def test_aliqout_not_in_manifest_contents(self):
        ManifestData.objects.create(
            identifier='AAAAA-AAAA')
        a = AliquotData.objects.create(
            identifier='VBEEA-BBSS')
        ManifestData.objects.create(
            identifier='AAAAA-BBBB')
        ManifestData.objects.create(
            identifier='FFPOE-AALL')
        self.assertNotIn(a.identifier,
                         str(ManifestData.objects.all().filter(
                             identifier=a.identifier
                         )))

    @tag('92')
    def test_manifest_in_database(self):
        """Assert that a manifest exists on the database
        """
        mani = Manifest.objects.create()
        manifest = Manifest(manifest_identifier='M02ABCDQWERT')
        manifest_item = ManifestItem.objects.create(
            manifest=mani,
            identifier='AAAO-QWER-2RRR')
        self.assertFalse(manifest.manifest_on_database)
        ReceiveAliquot(manifest=manifest, aliquot=self.aliquot,
                       manifest_item=manifest_item)
        self.assertTrue(manifest.manifest_on_database)

    @tag('93')
    def test_manifest_not_in_database(self):
        """Assert that a manifest is not in the database
        """
        manifest = Manifest(manifest_identifier='M01ZXCVBASDF')
        ReceiveAliquot(manifest=manifest, aliquot=self.aliquot,
                       manifest_item=self.manifest_item)
        self.assertFalse(manifest.manifest_on_database)
