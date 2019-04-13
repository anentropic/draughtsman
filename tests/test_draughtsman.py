import unittest
from unittest import mock
import draughtsman
from refract.contrib.apielements import ParseResult, registry


class DraughtsmanTests(unittest.TestCase):
    def test_parse_valid_blueprint(self):
        parse_result = draughtsman.parse('# My API')

        self.assertIsInstance(parse_result, ParseResult)
        self.assertEqual(parse_result.api.title.defract, 'My API')

    def test_parse_valid_blueprint_with_source_maps(self):
        parse_result = draughtsman.parse('# My API', generate_source_map=True)

        self.assertIsInstance(parse_result, ParseResult)
        self.assertEqual(parse_result.api.title.defract, 'My API')
        self.assertEqual(
            parse_result.api.title.attributes.get('sourceMap').defract,
            [[[0, 8]]]
        )

    def test_custom_deserialiser(self):
        mock_init = mock.MagicMock(return_value=None)
        mock_deserialise = mock.MagicMock()

        class CustomDeserialiser:
            __init__ = mock_init
            deserialise = mock_deserialise

        draughtsman.parse('# My API', deserialiser_cls=CustomDeserialiser)

        mock_init.assert_called_once_with(
            registry=registry
        )
        self.assertEqual(mock_deserialise.call_count, 1)

    def test_custom_registry(self):
        mock_init = mock.MagicMock(return_value=None)
        mock_deserialise = mock.MagicMock()

        class CustomDeserialiser:
            __init__ = mock_init
            deserialise = mock_deserialise

        custom_registry = object()

        draughtsman.parse(
            '# My API',
            deserialiser_cls=CustomDeserialiser,
            custom_registry=custom_registry,
        )

        mock_init.assert_called_once_with(
            registry=custom_registry
        )
        self.assertEqual(mock_deserialise.call_count, 1)
