from unittest import TestCase
from unittest.mock import MagicMock

from src.application.use_cases import NGGUseCases
from src.adapters.input import NGGInputAdapter


class TestNGGInputAdapter(TestCase):
    adapter: NGGInputAdapter

    def setUp(self):
        use_cases = NGGUseCases()
        self.adapter = NGGInputAdapter(use_cases)

    def test_main(self):
        self.adapter.input_port.play = MagicMock(return_value=200)
        result = self.adapter.main()
        self.assertEqual(result, 0)
