class Question:
    """The Question-class describes a single question.

		TODO: Complete the next-method.
	"""

    def __init__(self, type):

        """Constuctor for the class.

        Parameters:
            type: Describes the "type" of the exercise, such as "Group theory",
            "Ring theory" and so forth.

        """
        self.type = type



    def next(self):
        return True