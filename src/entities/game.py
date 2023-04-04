class Game:
    """The Game-class describes the algebra "game" that the user plays."""

    def __init__(self, player, mode):
        """Constructor for the class.

		Constructor parameters:
			player: Each game has a player.
			mode: The "mode" of the game, i.e., whether or not the user wants to
				  practice definitions, proofs or solve multiple choice question and so forth.
				  A mode can be changed or it can contain multiple choices as a list.
		"""

        self.player = player
        self.mode = mode

    def fetch_exercise(self, type=None):
        """Fetches an exercise to be completex next.

		Parameters:
			type: Describes the "type" of the exercise, such as "Group theory",
			"Ring theory" and so forth.

		"""
        pass
        #exercise = Exercise(type)
        #exercise.fetch_question()

    def play(self):
        """Executes the game
        TODO: Implement
        """
        pass