from question import Question
class Exercise:
    """The Exercise-class that describes a singleton exercise.

       TODO: Factor into a superclass and use inheritance for different type of exercises.
    """


    def __init__(self, difficulty, type=None):
        self.type = type
        """Constuctor for the class.
    
         Parameters:
             type: Describes the "type" of the exercise, such as "Group theory",
             "Ring theory" and so forth.
    
             difficulty: Difficulty of the wished exercises.	
    
         """


    def fetch_question(self):
        question = Question(type)
        return question.next()


