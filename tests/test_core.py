import unittest

from core.engine import ZalZalaEngine


class TestZalZala(unittest.TestCase):

    def test_url_normalization(self):
        engine = ZalZalaEngine("example.com")
        self.assertEqual(
            engine.normalize_target(),
            "https://example.com"
        )

    def test_valid_target(self):
        engine = ZalZalaEngine("https://example.com")
        self.assertTrue(engine.validate_target())


if __name__ == "__main__":
    unittest.main()
