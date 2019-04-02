import csv
from enum import Enum

import numpy as np

from forms.exceptions import ImproperFormatException, \
    InconsistentAppStateException


class AppState:
    location = None

    answer_list = None  # type: list
    answer_set_stats = None  # type: dict

    current_question = None  # type: str
    current_answer_set = None  # type: dict

    def __init__(self, location):
        self.file_location = location
        self._load_data(self.file_location)

    def get_next_question(self) -> str:
        """
        Returns next question for our candidate.

        :return:
        """
        return "SASDQASDSD"

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
        try:
            self.answer_list = []
            with open(location) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.answer_list.append(row)

        except csv.Error:
            raise ImproperFormatException

        self._calculate_stats()

    def save_dataset(self):
        """
        Handler for saving data with current poll to dataset
        :return:
        """
        pass

    def _calculate_stats(self):
        """
        Calculates stats for provided dataset.

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
                if element.get(key) == "T":
                    key_count = key_count + 1

            self.answer_set_stats[key] = key_count

