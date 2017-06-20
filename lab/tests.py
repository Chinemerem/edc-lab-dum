import re

from django.test import TestCase,tag
from django.utils import timezone

from .models.box import Box
from .models.aliquot import Aliquot
from .identifiers.aliquot_identifiers import AliquotIdentifier




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
        
    

@tag('aliquotIdentifier')
class TestAliquotIdentifier(TestCase):

    def test_aliquot_identifier(self):
        AliquotIdentifier(
            identifier_prefix='2345678109',
            numeric_code='22',
            count_padding=2,
            identifier_length=18)