from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.application.use_cases import NGGUseCases
from src.adapters.input import NGGInputAdapter


class TestNGGInputAdapter(TestCase):
    adapter: NGGInputAdapter

    def setUp(self):
        use_cases = NGGUseCases()
        self.adapter = NGGInputAdapter(use_cases)

    @patch("builtins.input", side_effect=["y", "y", "n"])
    def test_main(self, input_mock):
        self.adapter.input_port.play = MagicMock(return_value=200)
        result = self.adapter.main()
        self.assertEqual(result, 0)
        self.assertEqual(input_mock.call_count, 3)
