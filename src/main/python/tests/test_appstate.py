import unittest

from forms.appstate import AppState


class TestAppState(unittest.TestCase):

    def setUp(self) -> None:
        self.appstate = AppState(None)
        self.appstate.answer_list = [
            {
                'mock_1': "F",
                'mock_2': "F"
            },
            {
                'mock_1': "T",
                'mock_2': "T"
            }
        ]

        self.appstate.current_answer_set = {
            'mock_1': "-",
            'mock_2': "-"
        }

        self.appstate.answer_set_stats = {
            'mock_1': 1,
            'mock_2': 1
        }

    def test_chance_estimation(self):
        self.assertEqual(
            self.appstate.get_chance(),
            50
        )

    def test_progress(self):
        self.appstate.get_next_question()
        self.assertEqual(
            self.appstate.get_progress(),
            0
        )
        self.appstate.mark_true()
        self.appstate.get_next_question()

        self.assertEqual(
            self.appstate.get_progress(),
            50
        )

    def test_marking_true(self):
        self.assertRaises(
            Exception,
            self.appstate.mark_true()
        )

    def test_marking_false(self):
        self.assertRaises(
            Exception,
            self.appstate.mark_false()
        )

    def test_marking_unanswered(self):
        self.assertRaises(
            Exception,
            self.appstate.mark_false()
        )

    def test_saving(self):
        self.appstate.mark_false()
        self.appstate.get_next_question()
        self.appstate.mark_false()
        self.assertRaises(
            Exception,
            self.appstate.save_dataset('save_mock_data.csv')
        )

