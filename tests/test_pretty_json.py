from datetime import datetime
from unittest import TestCase

import pretty_json


class PrettyJsonTest(TestCase):

    def test_pretty_print_is_str(self):
        self.assertIsInstance(pretty_json.pretty_print({'foo': 'bar'}), str)

    def test_pretty_print_with_date_is_str(self):
        self.assertIsInstance(
            pretty_json.pretty_print({'foo': 'bar', 'now': datetime.now()}),
            str
        )

    def test_format_json_is_unicode(self):
        # type will be unicode when python version is 2
        try:
            is_type = unicode
        except:
            is_type = str
        self.assertIsInstance(
            pretty_json.format_json({'foo': 'bar', 'int': 5}),
            is_type
        )
