class QuestionsEnded(Exception):
    """
        Raised when there are no more questions left for our candidate.
    """



class QuestionAnsweredFalsely(Exception):
    """
        Raised when our candidate answered falsely.
    """


class QuestionUnanswered(Exception):
    """
        Raised when our candidate did not answer the question.
    """
