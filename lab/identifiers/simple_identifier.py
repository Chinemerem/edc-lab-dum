import random

from django.apps import apps as django_apps


class DuplicateIdentifierError(Exception):
    pass


class SimpleIdentifier:

    random_string_length = 5
    model = None
    error_class = DuplicateIdentifierError
    template = '{device_id}{random_string}'

    def __init__(self, model=None, identifier_type=None):
        edc_device_app_config = django_apps.get_app_config('edc_device')
        self.model = model or self.model
        device_id = edc_device_app_config.device_id
        self.identifier = self.template.format(
            device_id=device_id, random_string=self.random_string)

    def __str__(self):
        return self.identifier

    @property
    def random_string(self):
        return ''.join(
            [random.choice('ABCDEFGHKMNPRTUVWXYZ2346789') for _ in range(
                self.random_string_length)])


class SimpleUniqueIdentifier:

    """Usage:
        class ManifestIdentifier(Identifier):
            random_string_length = 9
            identifier_attr = 'manifest_identifier'
            template = 'M{device_id}{random_string}'
    """

    random_string_length = 5
    identifier_type = 'simple_identifier'
    identifier_attr = 'identifier'
    model = None
    error_class = DuplicateIdentifierError
    template = '{device_id}{random_string}'

    def __init__(self, model=None, identifier_type=None):
        edc_device_app_config = django_apps.get_app_config('edc_device')
        self._simple_identifier = SimpleIdentifier()
        self.model = model or self.model
        self.identifier_type = identifier_type or self.identifier_type
        self.device_id = edc_device_app_config.device_id
        self.identifier = self._simple_identifier.identifier
        if self.is_duplicate:
            raise self.error_class(
                'Unable prepare a unique identifier, '
                'all are taken. Increase the length of the random string')
        self.save()

    def save(self):
        self.model_class.objects.create(
            identifier_type=self.identifier_type,
            **{self.identifier_attr: self.identifier})

    @property
    def model_class(self):
        return django_apps.get_model(*self.model.split('.'))

    @property
    def is_duplicate(self):
        is_duplicate = False
        if self.model_class.objects.filter(
                identifier_type=self.identifier_type,
                **{self.identifier_attr: self.identifier}):
            n = 1
            while self.model_class.objects.filter(
                    identifier_type=self.identifier_type
                    **
                    {self.identifier_attr: self.identifier}):
                self.identifier = self._simple_identifier.identifier
                n += 1
                if n == len('ABCDEFGHKMNPRTUVWXYZ2346789') **\
                        self.random_string_length:
                    is_duplicate = True
        return is_duplicate
