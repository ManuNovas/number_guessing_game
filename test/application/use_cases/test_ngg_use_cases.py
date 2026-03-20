from unittest import TestCase

from src.application.use_cases import NGGUseCases


class TestNGGUseCases(TestCase):
    use_cases: NGGUseCases

    def setUp(self):
        self.use_cases = NGGUseCases()

    def test_start(self):
        self.use_cases.start()
        self.assertGreaterEqual(self.use_cases.score.number, 1)
        self.assertLessEqual(self.use_cases.score.number, 100)
