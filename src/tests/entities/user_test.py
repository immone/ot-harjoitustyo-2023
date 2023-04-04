import unittest
from src.entities.game import Game
from src.entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user = User("kalle", "Easy")
        self.game = Game(self.user, ["def"])
        
    def test_default_difficulty(self):
        usertwo = User("jaakko")
        self.assertEqual(usertwo.return_difficulty(), "Medium")
        
    def test_difficulty_with_parameter(self):
        self.assertEqual(self.user.return_difficulty(), "Easy")