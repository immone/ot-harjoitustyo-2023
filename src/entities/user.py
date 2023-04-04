class User:
    """The User-class describes the player that is created upon launching the application.

        TODO: Create classes for the different difficulties and refactor.
    """

    def __init__(self, name, difficulty=None):
        """ Constructor for the class.

            Constructor parameters:
                name: Name of the player
                difficulty: The difficulty that the user wishes to "play" on.

            Attributes:
                points: Describes the points (mapped to some scale) that the user has cumulated
                during its "session".

        """
        self.difficulty = difficulty
        if difficulty == None:
            self.difficulty = "Medium"

        self.points = 0


    def change_difficulty(self, new_difficulty):
        """ Changes the difficulty for the user.

            Attributes:
            new_difficulty: The new difficulty that the user wishes to play on.

        """
        self.difficulty = new_difficulty


    def return_difficulty(self):
        """ Returns the current difficulty.
        """
        return self.difficulty
