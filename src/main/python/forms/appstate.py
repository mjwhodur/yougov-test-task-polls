
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

    def save_dataset(self):
        """
        Handler for saving data to current dataset
        :return:
        """
        pass
