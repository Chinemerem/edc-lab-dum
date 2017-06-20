import re

from django.test import TestCase,tag
from django.utils import timezone
from django.db.utils import IntegrityError

from .models.box import Box
from .model_mixins.aliquot_model_mixin import AliquotModelMixin



class TestBox(TestCase):
    
    pattern = '^[A-Z]{3}\-[0-9]{4}\-[0-9]{2}$'
    
    @tag('pattern')
    def test_pattern(self):
        box = Box(box_identifier = 'adebdjshiq8e9qe', name ='make', category='testing')
        self.assertTrue(re.match(self.pattern, box.box_identifier))
        
    @tag('identifier')    
    def test_identifier(self):
        box1 = Box(box_identifier = 'adebdjshiq8e9qe', name ='make', category='testing', box_datetime = timezone.now())
        self.assertEqual('ASE890645', box1.box_identifier)
        
    

@tag('aliquot')
class TestAliquot(TestCase):

    def test_aliquot_model_constraint(self):
        AliquotModelMixin.objects.create(count=0)
        self.assertRaises(
            IntegrityError,
            aliquot=AliquotModelMixin.objects.create, count=0)
