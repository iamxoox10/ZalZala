import unittest

from core.engine import ZalZalaEngine


class TestZalZala(unittest.TestCase):

    def test_normalization(self):

        engine = ZalZalaEngine(
            "example.com"
        )

        self.assertEqual(
            engine.target,
            "https://example.com"
        )

    def test_validation(self):

        engine = ZalZalaEngine(
            "https://example.com"
        )

        self.assertTrue(
            engine.valid()
        )


if __name__ == "__main__":
    unittest.main()