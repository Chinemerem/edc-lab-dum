from .simple_identifier import SimpleIdentifier


class BoxIdentifier(SimpleIdentifier):

    random_string_length = 9
    identifier_type = 'box_identifier'
    template = 'B{device_id}{random_string}'
