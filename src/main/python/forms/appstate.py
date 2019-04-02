import csv

import numpy as np

from forms.exceptions import (
    ImproperFormatException,
    InconsistentAppStateException,
    QuestionsEnded
)


class AppState:
    location = None

    answer_list = []  # type: list
    answer_set_stats = {}  # type: dict

    current_question = None
    current_answer_set = {}  # type: dict

    _ever_clicked_not_false = False

    def __init__(self, location):
        self.chance = 100
        self.progress = 0
        self.file_location = location

    def load_data(self):
        """
        Interface for loading data.
        :return:
        """
        self._load_data(self.file_location)

    def get_next_question(self) -> str:
        """
        Returns next question for our candidate.

        :return:
        """
        if not self.current_question:
            self._set_question()

        return self.current_question

    def get_chance(self) -> int:
        """
        Returns chance of current candidate to fit our profile
        :return:
        """
        self._calculate_chance()

        return self.chance

    def get_progress(self) -> int:
        """
        Returns current progress
        :return: progress : int
        """
        self._update_progress()
        return self.progress

    def mark_true(self):
        """
        Marks question as answered as True.
        :return:
        """
        self._mark_true()

    def mark_false(self):
        """
        Marks question as answered as False.

        :return:
        """
        self._mark_false()

    def mark_no_answer(self):
        """
        Marks question as unanswered.

        :return: None
        """
        self._mark_no_answer()

    def save_dataset(self, filename):
        """
        Handler for saving data with current poll to dataset
        :return:
        """
        self._save_data(filename)

    def _calculate_initial_stats(self):
        """
        Calculates stats for provided dataset and sets initial parameters for
        current answers set.

        :return:
        """
        self.answer_set_stats = {}
        if not len(self.answer_list) and isinstance(self.answer_list, list):
            raise InconsistentAppStateException

        if not isinstance(self.answer_list[0], dict):
            raise InconsistentAppStateException

        keys = self.answer_list[0].keys()

        for key in keys:

            key_count = 0

            for element in self.answer_list:
                if element.get(key) == "F":
                    key_count = key_count + 1

            self.answer_set_stats[key] = key_count
            self.current_answer_set[key] = "-"
            self._calculate_chance()
            self._update_progress()

    def _update_progress(self):
        """
        Private method for calculating current progress in percents
        :return:
        """

        answered_count = 0

        for key in self.current_answer_set.keys():
            if not self.current_answer_set[key] == '-':
                answered_count = answered_count + 1

        if answered_count == 0:
            self.progress = 0
        else:
            self.progress = float(float(answered_count) / len(
                self.current_answer_set.keys())) * 100

    def _mark_true(self):
        """
        Private method containing logic for marking questions.
        :return:
        """
        self._ever_clicked_not_false = True
        self.current_answer_set[self.current_question] = "T"
        self.current_question = None

    def _save_data(self, filename):
        """
        Saves data on finish of the poll

        :return: None
        """
        fieldnames = self.current_answer_set.keys()

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for element in self.answer_list:
                writer.writerow(element)

            writer.writerow(self.current_answer_set)

    def _calculate_chance(self):
        """
        Calculates and returns probability of our candidate to fit our profile.

        :return:
        """
        if self._ever_clicked_not_false:
            self.chance = 0
            return

        count_answered_false = 0
        num_keys_unanswered = 0

        for key in self.current_answer_set.keys():
            if self.current_answer_set[key] == '-':
                count_answered_false = (count_answered_false
                                        + self.answer_set_stats[key])
                num_keys_unanswered = num_keys_unanswered + 1

        if not num_keys_unanswered == 0:
            self.chance = int(count_answered_false / (
                    len(self.answer_list) * num_keys_unanswered) * 100)
        else:
            self.chance = 100
            self.progress = 100

    def _set_question(self):
        """
        Sets random possible question.
        :return:
        """

        possible_questions = []
        for key in self.current_answer_set.keys():
            if self.current_answer_set[key] == "-":
                possible_questions.append(key)

        if possible_questions:
            self.current_question = np.random.choice(possible_questions)
        else:
            raise QuestionsEnded

    def _load_data(self, location):
        """
        Gets data to provide calculations for questions. Requires CSV file.
        :param location: path to CSV file
        :return:
        """
        try:
            self.answer_list = []
            with open(location) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.answer_list.append(row)

        except csv.Error:
            raise ImproperFormatException

        self._calculate_initial_stats()

    def _mark_false(self):
        """
        Private method containing logic for marking questions.
        :return:
        """
        self.current_answer_set[self.current_question] = "F"
        self.current_question = None

    def _mark_no_answer(self):
        """
        Private method containing logic for marking questions.
        :return:
        """
        self._ever_clicked_not_false = True
        self.current_answer_set[self.current_question] = "U"
        self.current_question = None
