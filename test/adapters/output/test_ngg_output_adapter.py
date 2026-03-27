from unittest import TestCase
from unittest.mock import patch, mock_open, MagicMock

from src.domain.entites import Score
from src.adapters.output import NGGOutputAdapter


class TestNGGOutputAdapter(TestCase):
    adapter: NGGOutputAdapter

    def setUp(self):
        self.adapter = NGGOutputAdapter("test.json")

    @patch("src.adapters.output.ngg_output_adapter.exists")
    def test_get_next_id_without_data(self, mock_exists):
        mock_exists.return_value = False
        with patch("builtins.open", mock_open()) as mock_write:
            result = self.adapter.get_next_id()
            self.assertEqual(result, 1)
            mock_write.assert_called_with("test.json", "w")

    @patch("src.adapters.output.ngg_output_adapter.exists")
    def test_get_next_id_with_data(self, mock_exists):
        mock_exists.return_value = True
        with patch("builtins.open", mock_open(read_data='[{"id": 1}]')) as mock_read:
            result = self.adapter.get_next_id()
            self.assertEqual(result, 2)
            mock_read.assert_called_with("test.json", "r")

    def test_create(self):
        self.adapter._open = MagicMock()
        self.adapter._save = MagicMock()
        self.adapter.data = []
        score = Score(1, 1, 5, "00:00:10")
        self.adapter.create(score.__dict__)
        self.assertEqual(self.adapter.data, [score.__dict__])

    def test_sort_by_asc(self):
        self.adapter._open = MagicMock()
        self.adapter.data = [
            {
                "id": 1,
                "attempts": 5
            },
            {
                "id": 2,
                "attempts": 2
            },
            {
                "id": 3,
                "attempts": 3
            },
        ]
        result = self.adapter.sort_by("attempts", "asc")
        self.assertEqual(result, [
            {
                "id": 2,
                "attempts": 2
            },
            {
                "id": 3,
                "attempts": 3
            },
            {
                "id": 1,
                "attempts": 5
            },
        ])

    def test_sort_by_asc(self):
        self.adapter._open = MagicMock()
        self.adapter.data = [
            {
                "id": 1,
                "attempts": 5
            },
            {
                "id": 2,
                "attempts": 2
            },
            {
                "id": 3,
                "attempts": 3
            },
        ]
        result = self.adapter.sort_by("attempts", "desc")
        self.assertEqual(result, [
            {
                "id": 1,
                "attempts": 5
            },
            {
                "id": 3,
                "attempts": 3
            },
            {
                "id": 2,
                "attempts": 2
            },
        ])
