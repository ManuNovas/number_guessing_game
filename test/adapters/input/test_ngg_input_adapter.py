from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.domain.entites import Score
from src.adapters.output import NGGOutputAdapter
from src.application.use_cases import NGGUseCases
from src.adapters.input import NGGInputAdapter


class TestNGGInputAdapter(TestCase):
    adapter: NGGInputAdapter

    def setUp(self):
        output_adapter = NGGOutputAdapter("test.json")
        output_adapter.get_next_id = MagicMock(return_value=1)
        output_adapter.create = MagicMock()
        use_cases = NGGUseCases(output_adapter)
        self.adapter = NGGInputAdapter(use_cases)

    @patch("builtins.input", side_effect=["1", "y", "y", "n"])
    def test_main_play(self, input_mock):
        self.adapter.input_port.play = MagicMock(return_value=200)
        result = self.adapter.main()
        self.assertEqual(result, 0)
        self.assertEqual(input_mock.call_count, 4)

    @patch("builtins.input", side_effect=["2"])
    def test_main_play(self, input_mock):
        self.adapter.input_port.get_high_scores = MagicMock(return_value=[
            Score(3, 3, 2, "00:00:02"),
            Score(2, 2, 3, "00:00:04"),
            Score(1, 1, 5, "00:00:16")
        ])
        result = self.adapter.main()
        self.assertEqual(result, 0)
        self.assertEqual(input_mock.call_count, 1)
