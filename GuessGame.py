from random import seed
from random import randint

# by yaron zvi 24/11/2019 for devops course project

class GuessGame:
    def __init__(self,secretnumber = None,user_guess = None):
        self.secretnumber  = secretnumber
        self.user_guess =  user_guess

    def get_difficulty_from_user(self):
        print ('Guess game - please enter max number of game ')
        maxnumber = float(input())
        if ( maxnumber == 0  or maxnumber == 1   ):
            print ('yoy enterd worng number please start again')
            return 0
        else:
            return maxnumber

    def generate_number(self):
        seed(1)
        self.secretnumber  = randint(1,self.difficulty)
#       i use print here only for test
#        print('secret number ',self.secretnumber)
        return self.secretnumber

    def get_guess_from_user(self):
        print ('please enter your guess:')
        self.user_guess = int(input())
        return self.user_guess

    def compare_results(self):
        if (self.user_guess == self.secretnumber):
            return 1
        else:
            return 0

    def play(self):
        self.difficulty = GuessGame.get_difficulty_from_user(self)
        print('max number', self.difficulty)
        self.secretnumber = GuessGame.generate_number(self)
        self.guess = GuessGame.get_guess_from_user(self)
        self.result = GuessGame.compare_results(self)
        return self.result