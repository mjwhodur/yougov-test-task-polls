import unittest

from forms.appstate import AppState


class TestInterfaceWithoutAppState(unittest.TestCase):

    def setUp(self) -> None:
        self.appstate = AppState(None)
        self.appstate.answer_list = [
            {
                'mock_1' : "F",
                'mock_2' : "F"
            },
            {
                'mock_1': "T",
                'mock_2': "T"
            }
        ]

        self.appstate.current_answer_set = {
            'mock_1' : "-",
            'mock_2' : "-",
        }

    def test_data_loading_incorrect_file(self):
        pass

    def test_data_loading(self):
        pass

    def test_questioning(self):
        pass

    def test_questioning_answer_not_clicked(self):
        pass

    def test_chance_estimation(self):
        self.assertEqual(
            self.appstate.get_chance(),
            50
        )

    def test_progress(self):
        pass

    def test_marking_true(self):
        pass

    def test_marking_false(self):
        pass

    def test_marking_unanswered(self):
        pass

    def test_saving(self):
        pass


