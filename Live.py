from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRoulette import  CurrencyRoulette
from currency_converter import CurrencyConverter

# by yaron zvi 24/11/2019 for devops course project

class WorldOfGames:
    def __init__(self,name):
        self.player_name = WorldOfGames.welcome(name)
        self.clear = "\n" * 1000
        self.load_game = WorldOfGames.load_game()
        self.gamedifficulty = int(WorldOfGames.get_difficulty())
        self.valuesdict = [None] * self.gamedifficulty
        self.userlist = [None] * self.gamedifficulty
        self.c = CurrencyConverter()
        self.current_usd_to_ils = self.c.convert(1, 'USD', 'ILS')

#       i use print here only for test
#        print (self.player_name+' choose game number '+str(self.load_game)+' with difficulty level '+str(self.gamedifficulty))
        if (self.load_game == 2):
            self.lostorwon = GuessGame.play(self)
            if  (self.lostorwon == 1):
                print('you win')
            else:
                print('you lose')
        elif (self.load_game == 1):
            self.lostorwon = MemoryGame.play(self,self.gamedifficulty)
            if (self.lostorwon == 1):
                print('you win')
            else:
                print('you lose')
        elif (self.load_game == 3):
            self.lostorwon = CurrencyRoulette.play(self, self.gamedifficulty)
            if (self.lostorwon == 1):
                print('you win')
            else:
                print('you lose')
        print('end')
#123
# 10.11.2019 by yaron zvi - devops course
#This function has a person name as an input and returns a string in the following layout:
    def welcome(name):
        print ('Hello '+name+' and welcome to the World of Games (WoG).')
        print('Here you can find many cool games to play.')
        return name
#This function prints out the following text:
    def load_game():
        option = [1, 2, 3]
        print('Please choose a game to play:')
        print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
        print('2. Guess Game - guess a number and see if you chose like the computer')
        print('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
        gameoption = float(input())
        if (gameoption not in option):
            print('you didnt enter option 1 2 or  3 please try again')
            return 0
        else:
            return gameoption

    def get_difficulty():
        difficulty = [1, 2, 3, 4, 5]
        print('Please choose game difficulty from 1 to 5:')
        gamedifficulty = float(input())
        if (gamedifficulty not in difficulty ):
           print('you didnt enter difficulty 1 to 5 please try again ')
           return 0
        else:
            return gamedifficulty


