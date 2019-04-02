import csv
from enum import Enum

import numpy as np

from forms.exceptions import (
    ImproperFormatException,
    InconsistentAppStateException
)


class AppState:
    location = None

    answer_list = []  # type: list
    answer_set_stats = {}  # type: dict

    current_question = None  # type: str
    current_answer_set = {}  # type: dict

    def __init__(self, location):
        self.chance = None
        self.progress = None
        self.file_location = location
        self._load_data(self.file_location)

    def get_next_question(self) -> str:
        """
        Returns next question for our candidate.

        :return:
        """
        return self.current_question

    def get_chance(self) -> int:
        """
        Returns chance of current candidate to fit our profile
        :return:
        """
        self._get_chance()
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

    def save_dataset(self):
        """
        Handler for saving data with current poll to dataset
        :return:
        """
        pass

    def _calculate_stats(self):
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
                if element.get(key) == "T":
                    key_count = key_count + 1

            self.answer_set_stats[key] = key_count
            self.current_answer_set[key] = None
            self._get_chance()
            self._update_progress()

    def _update_progress(self):
        pass

    def _get_chance(self):
        pass

    def _mark_true(self):
        """
        Private method containing logic for marking questions.
        :return:
        """

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

    def _mark_false(self):
        """
        Private method containing logic for marking questions.
        :return:
        """
        pass

    def _mark_no_answer(self):
        """
        Private method conatining logic for marking questions.
        :return:
        """
        pass

    def _set_question(self):
        pass
