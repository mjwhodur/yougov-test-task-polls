# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, \
    QHBoxLayout, QProgressBar, QLayout, QVBoxLayout


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.interface_builder()

    def interface_builder(self):
        app_grid = QGridLayout()

        question_label = QLabel("Question: ", self)
        question_text = QLabel("MainWindow.question_text", self)

        true_button = QPushButton("True", self)
        false_button = QPushButton("False", self)
        wont_answer_button = QPushButton("Won't answer", self)
        load_questions_data = QPushButton("Load question data")

        button_layout = QHBoxLayout()
        button_layout.addWidget(true_button)
        button_layout.addWidget(false_button)
        button_layout.addWidget(wont_answer_button)
        button_layout.addWidget(load_questions_data)

        question_layout = QHBoxLayout()
        question_layout.addWidget(question_label)
        question_layout.addWidget(question_text)

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

        def load_questions_data_click():
            pass

        def click_true():
            pass

        def click_false():
            pass

        def click_no_answer():
            pass
