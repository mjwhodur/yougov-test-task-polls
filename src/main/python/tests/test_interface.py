import unittest
from sys import argv

from PyQt5.QtWidgets import QApplication
from forms.general import MainWindow


class TestInterfaceWithoutAppState(unittest.TestCase):

    def setUp(self) -> None:
        self.app = QApplication(argv)
        self.window = MainWindow()

    def test_click_true(self):
        self.assertRaises(
            Exception,
            self.window.true_button.click(),
        )
        self.window.close()

    def test_click_false(self):
        self.assertRaises(
            Exception,
            self.window.false_button.click(),
        )
        self.window.close()

    def test_click_unanswered(self):
        self.assertRaises(
            Exception,
            self.window.wont_answer_button.click(),
        )
        self.window.close()

    def test_click_open_dialog(self):
        self.assertRaises(
            Exception,
            self.window.load_questions_data.click(),

        )
        self.window.close()
