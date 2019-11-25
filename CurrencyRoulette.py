from random import seed
from random import randint

# by yaron zvi 24/11/2019 for devops course project

class CurrencyRoulette():
    def __init__(self,gamedifficulty):
        self.gamedifficulty = gamedifficulty
        self.interval = None

    def get_money_interval(self):
        return (5-self.gamedifficulty)

    def get_guess_from_user(self):
        print('guess how many ILS is ',self.rendom_1_to_100,' USD')
        self.guessanswer = int(input())
        return self.guessanswer

    def play(self,gamedifficulty):
#       i use print here only for test
#        print('rate ', self.current_usd_to_ils)
        seed(1)
        self.rendom_1_to_100 = randint(1, 100)
#       i use print here only for test
#        print('number 1 to 100 ',self.random_1_to_100)
        self.interval = CurrencyRoulette.get_money_interval(self)
#       i use print here only for test
#        print('interval',self.interval)
#        print('answer ',self.rendom_1_to_100 * self.current_usd_to_ils)
        self.guessanswer = CurrencyRoulette.get_guess_from_user(self)
        if ( self.guessanswer >= ((self.rendom_1_to_100 * self.current_usd_to_ils)-self.interval) and
                self.guessanswer <= ((self.rendom_1_to_100 * self.current_usd_to_ils)+self.interval)):
            return 1
        else:
            return 0




