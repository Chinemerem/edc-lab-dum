# from django.test import TestCase, tag
#
#
# from ..identifiers import AliquotIdentifierLengthError,\
#     AliquotIdentifierCountError, AliquotIdentifier
# from ..identifiers import Prefix, PrefixLengthError,\
#     PrefixKeyError, PrefixMissingLengthError
#
#
# @tag('aliquotIdentifier')
# class TestAliquotIdentifier(TestCase):
#
#     @tag('validLength')
#     def test_valid_length(self):
#         print(AliquotIdentifier(
#             identifier_prefix='2345678109',
#             numeric_code='27',
#             count_padding=2,
#             identifier_length=18))
#
#     @tag('lenghtRaises')
#     def test_length_raises(self):
#         """Asserts raises exception for invalid identifier length.
#         """
#         self.assertRaises(
#             AliquotIdentifierLengthError,
#             AliquotIdentifier,
#             identifier_prefix='1234567890',
#             count_padding=2,
#             identifier_length=18)
#
#     @tag('numericCode')
#     def test_numeric_code(self):
#         identifier = AliquotIdentifier(
#             identifier_prefix='XXXXXXXX',
#             numeric_code='02',
#             count_padding=2,
#             identifier_length=16)
#         self.assertIn('02', str(identifier))
#
#     """Asserts if an identifier is primary .Change the
#      assertTrue to be false to make the tests fail
#     """
#
#     def test_primary(self):
#         identifier = AliquotIdentifier(
#             identifier_prefix="XXXXXXXX",
#             numeric_code='11',
#             count_padding=2,
#             identifier_length=16)
#         self.assertIn('0000', str(identifier))
#         self.assertTrue(identifier.is_primary)
#
#     @tag('primaryNeeds')
#     def test_not_primary_needs_count(self):
#         """
#         """
#         self.assertRaises(AliquotIdentifierCountError,
#                           AliquotIdentifier,
#                           parent_segment="0201",
#                           identifier_prefix='XXXXXXXX',
#                           numeric_code='11',
#                           count=2,
#                           count_padding=2,
#                           identifier_length=16)
#
#     @tag('parentSegment')
#     def test_not_primary_parent_segment(self):
#         identifier = AliquotIdentifier(
#             parent_segment='1102',
#             identifier_prefix='XXXXXXXX',
#             numeric_code='11',
#             count=222,
#             count_padding=2,
#             identifier_length=17)
#         self.assertIn('1102', str(identifier))
#         self.assertFalse(identifier.is_primary)
#
#     @tag('lengthError')
#     def test_large_count_raises_length_error(self):
#         self.assertRaises(
#             AliquotIdentifierLengthError,
#             AliquotIdentifier,
#             parent_segment='0201',
#             identifier_prefix='XXXXXXXX',
#             numeric_code='11',
#             count=222,
#             count_padding=2,
#             identifier_length=16)
#
#     @tag('countValid')
#     def test_large_count_valid(self):
#         try:
#             AliquotIdentifier(
#                 parent_segment='0201',
#                 identifier_prefix='XXXXXXXX',
#                 numeric_code='11',
#                 count=222,
#                 count_padding=2,
#                 identifier_length=17)
#         except AliquotIdentifierLengthError:
#             self.fail('AliquotIdentifierLengthError unexpectedly raised.')
#
#
# class TestAliquotPrefix(TestCase):
#
#     """Failed """
#     @tag('prefix')
#     def test_prefix(self):
#         prefix_obj = Prefix(
#             template='{opt1}{opt2}',
#             length=8,
#             opt1='opt1', opt2='opt2')
#         self.assertEqual(str(prefix_obj), 'opt1opt2')
#
#     @tag('notPrefix')
#     def test_invalid_prefix(self):
#         prefix_obj = Prefix(
#             template='{opt1}{opt2}',
#             length=8,
#             opt1='opt1', opt2='opt2')
#         self.assertEqual(str(prefix_obj), 'opt1opt2')
#
#     @tag('invalidLength')
#     def test_prefix_invalid_length(self):
#         self.assertRaises(PrefixLengthError, Prefix,
#                           template='{opt1}{opt2}',
#                           length=7,
#                           opt1='opt1', opt2='opt2')
#
#     @tag('prefixvalidLength')
#     def test_prefix_valid_length(self):
#         self.assertRaises(PrefixLengthError, Prefix,
#                           template='{opt}{opt2}',
#                           length=7,
#                           opt='op1',
#                           opt2='opt2')
#
#     @tag('length')
#     def test_length_none(self):
#         self.assertRaises(PrefixMissingLengthError, Prefix,
#                           template='{opt1}{opt2}',
#                           opt1='opt10',
#                           opt2='opt2')
#
#     @tag('missingOpt')
#     def test_prefix_missing_opt(self):
#         self.assertRaises(
#             PrefixKeyError,
#             Prefix,
#             template='{opt1}{opt2}',
#             length=8,
#             opt1='opt1')
#
#     @tag('opt')
#     def test_prefix_opt(self):
#         self.assertRaises(
#             PrefixKeyError,
#             Prefix,
#             template='{opt1}{opt2}{opt3}',
#             length=9,
#             opt1='opt1',
#             opt2='op7',
#             opt3='90')
