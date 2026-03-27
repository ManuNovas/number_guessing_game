from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.adapters.output import NGGOutputAdapter
from src.application.use_cases import NGGUseCases


class TestNGGUseCases(TestCase):
    use_cases: NGGUseCases

    def setUp(self):
        output_adapter = NGGOutputAdapter("test.json")
        output_adapter.get_next_id = MagicMock(return_value=1)
        output_adapter.create = MagicMock()
        self.use_cases = NGGUseCases(output_adapter)

    @patch("builtins.input", side_effect=["1", "10", "90", "30", "80", "50"])
    @patch("src.application.use_cases.ngg_use_cases.randrange")
    def test_play_easy_win(self, mocked_randrange, mocked_input):
        mocked_randrange.return_value = 50
        result = self.use_cases.play()
        self.assertEqual(result, 200)
        self.assertEqual(mocked_input.call_count, 6)

    @patch("builtins.input", side_effect=["0"])
    def test_play_invalid_difficulty(self, mocked_input):
        result = self.use_cases.play()
        self.assertEqual(result, 400)
        self.assertEqual(mocked_input.call_count, 1)

    @patch("builtins.input", side_effect=["2", "10", "20", "30", "40", "50"])
    @patch("src.application.use_cases.ngg_use_cases.randrange")
    def test_play_medium_game_over(self, mocked_randrange, mocked_input):
        mocked_randrange.return_value = 60
        result = self.use_cases.play()
        self.assertEqual(result, 202)
        self.assertEqual(mocked_input.call_count, 6)

    @patch("builtins.input", side_effect=["3", "10", "20", "30"])
    @patch("src.application.use_cases.ngg_use_cases.randrange")
    def test_play_hard_win(self, mocked_randrange, mocked_input):
        mocked_randrange.return_value = 30
        result = self.use_cases.play()
        self.assertEqual(result, 200)
        self.assertEqual(mocked_input.call_count, 4)
