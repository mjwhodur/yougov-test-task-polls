# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QProgressBar,
    QLayout,
    QVBoxLayout
)

from forms.exceptions import (
    QuestionsEnded,
    QuestionAnsweredFalsely,
    QuestionUnanswered
)


class MainWindow(QWidget):
    """
        Main class for Form of our application. Handles input and output
    """
    appstate = None

    def __init__(self, parent=None):
        super().__init__()
        self.interface_builder()

    def interface_builder(self) -> None:
        """
        Creates main window interface
        :return: None
        """
        app_grid = QGridLayout()

        question_label = QLabel("Question: ", self)

        self.question_text = QLabel("MainWindow.question_text", self)

        true_button = QPushButton("True", self)
        true_button.clicked.connect(self.click_true)

        false_button = QPushButton("False", self)
        false_button.clicked.connect(self.click_false)

        wont_answer_button = QPushButton("Won't answer", self)
        wont_answer_button.clicked.connect(self.click_no_answer)

        load_questions_data = QPushButton("Load question data")
        load_questions_data.clicked.connect(self.click_no_answer)

        button_layout = QHBoxLayout()
        button_layout.addWidget(true_button)
        button_layout.addWidget(false_button)
        button_layout.addWidget(wont_answer_button)
        button_layout.addWidget(load_questions_data)

        question_layout = QHBoxLayout()
        question_layout.addWidget(question_label)
        question_layout.addWidget(self.question_text)

        pb_suitability = QProgressBar()
        pb_questions = QProgressBar()

        pb_layout = QVBoxLayout()
        pb_layout.addWidget(pb_suitability)
        pb_layout.addWidget(pb_questions)

        app_grid.addItem(question_layout, 0, 0)
        app_grid.addItem(pb_layout, 1, 0)
        app_grid.addItem(button_layout, 2, 0)

        self.setLayout(app_grid)

        self.resize(500, 500)
        self.setWindowTitle(
            "YouGov Polls"
        )
        self.show()

    def load_questions_data_click(self):
        """
        Handler for Load Questions Data button
        :return: None
        """

        if not self.appstate:
            self.appstate = AppState()
        else:
            pass

    def click_true(self):
        """
        Handler for click event of True button
        :return: None
        """

        if self.appstate:
            self.appstate.mark_true()
            self.set_layout_for_next_question()

    def click_false(self):
        """
        Handler for click event of False button
        :return: None
        """
        self.appstate.mark_false()
        self.set_layout_for_next_question()

    def click_no_answer(self):
        """
        Handler for click event of "no answer" button.
        :return:
        """

    def load_data(self):
        """
        handler of data loading for AppState class
        :return:
        """

    def set_layout_for_next_question(self):
        try:
            chance = self.appstate.get_chance()
            progress = self.appstate.get_progress()
            question = self.appstate.get_next_question()

        except QuestionsEnded:
            self.question_text.setText(
                "All questions have been answered."
            )

        except QuestionAnsweredFalsely:
            self.question_text.setText(
                "You have answered false to one or more questions. "
                "Poll cannot continue."
            )

        except QuestionUnanswered:
            self.question_text.setText(
                "You have not answered to one or more questions. "
                "Poll cannot continue."
            )

        else:
            self.question_text.setText(
                self.appstate.get_next_question()
            )


class AppState:
    location = None

    def __init__(self, location):
        self.file_location = location
        self._load_data(location)

    def get_next_question(self) -> str:
        """
        Returns next question for our candidate.

        :return:
        """

    def get_chance(self) -> int:
        """
        Returns chance of current candidate to fit our profile
        :return:
        """

    def get_progress(self) -> int:
        """
        Returns current progress
        :return: progress : int
        """

    def mark_true(self):
        """
        Marks question as answered as True.
        :return:
        """

    def mark_false(self):
        """
        Marks question as answered as False.

        :return:
        """
        pass

    def mark_no_answer(self):
        """
        Marks question as unanswered.

        :return: None
        """
        pass

    def _save_data(self):
        """
        Saves data on finish of the poll

        :return: None
        """
        pass

    def _calculate_chance(self) -> int:
        """
        Calculates and returns probability of our candidate to fit our profile.

        :return:
        """

    def _load_data(self, location):
        """
        Gets data to provide calculations for questions. Requires CSV file.
        :param location: path to CSV file
        :return:
        """
