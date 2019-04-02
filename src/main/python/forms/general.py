"""
    Module forms.general

    Contains classes for handling interaction between user and GUI
"""
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QProgressBar,
    QLayout,
    QVBoxLayout,
    QFileDialog, QMessageBox)

from forms.appstate import AppState
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

        self.question_text = QLabel("Load dataset first.", self)

        self.true_button = QPushButton("True", self)
        self.true_button.clicked.connect(self.click_true)

        self.false_button = QPushButton("False", self)
        self.false_button.clicked.connect(self.click_false)

        self.wont_answer_button = QPushButton("Won't answer", self)
        self.wont_answer_button.clicked.connect(self.click_no_answer)

        self.load_questions_data = QPushButton("Load question data")
        self.load_questions_data.clicked.connect(self.load_questions_data_click)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.true_button)
        self.button_layout.addWidget(self.false_button)
        self.button_layout.addWidget(self.wont_answer_button)
        self.button_layout.addWidget(self.load_questions_data)

        question_layout = QHBoxLayout()
        question_layout.addWidget(question_label)
        question_layout.addWidget(self.question_text)

        self.pb_suitability = QProgressBar()
        self.pb_questions = QProgressBar()
        self.pb_questions.setValue(0)
        self.pb_suitability.setValue(0)

        pb_layout = QVBoxLayout()
        pb_layout.addWidget(self.pb_suitability)
        pb_layout.addWidget(QLabel("Chance"))
        pb_layout.addWidget(self.pb_questions)
        pb_layout.addWidget(QLabel("Progress"))

        app_grid.addItem(question_layout, 0, 0)
        app_grid.addItem(pb_layout, 1, 0)
        app_grid.addItem(self.button_layout, 2, 0)

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

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)",
            options=options
        )
        if filename:

            if not self.appstate:
                self.appstate = AppState(filename)
            else:

                buttonReply = QMessageBox.question(
                    self, 'Polls', "Are you sure to discard all data?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )

                if buttonReply == QMessageBox.Yes:
                    self.appstate = AppState(filename)
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
        else:
            QMessageBox.about(
                self,
                "Error",
                "You'll need to provide dataset first."
            )

    def click_false(self):
        """
        Handler for click event of False button
        :return: None
        """
        if self.appstate:
            self.appstate.mark_false()
            self.set_layout_for_next_question()
        else:
            QMessageBox.about(
                self,
                "Error",
                "You'll need to provide dataset first."
            )

    def click_no_answer(self):
        """
        Handler for click event of "no answer" button.
        :return:
        """
        if self.appstate:
            self.appstate.mark_no_answer()
            self.set_layout_for_next_question()
        else:
            QMessageBox.about(
                self,
                "Error",
                "You'll need to provide dataset first."
            )

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

            QMessageBox.about(
                self,
                "All questions answered.",
                "You need to provide dataset filename to save."
            )

            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            filename, _ = QFileDialog.getSaveFileName(
                self,
                "QFileDialog.getSaveFileName()", "", "CSV Files (*.csv)",
                options=options
            )
            self.appstate.save_dataset()

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
                question
            )

            self.pb_questions.setValue(progress)
            self.pb_suitability.setValue(chance)
