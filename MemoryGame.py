from random import seed
from random import randint
import time

# by yaron zvi 24/11/2019 for devops course project

class MemoryGame():
    def __init__(self,gamedifficulty):
        self.gamedifficulty = gamedifficulty



    def generate_sequence(self):
        seed(1)
        for i  in range (self.gamedifficulty):
            self.valuesdict[i] = randint(1, self.gamedifficulty)
        print("Values : ", self.valuesdict)
# the values will by shwon only for 0.7 second
        time.sleep(.700)
        print(self.clear)
        return  self.valuesdict

    def get_list_from_user(self):
        print('Please enter the number one by one ,use with enter between them')
        for i in range (self.gamedifficulty):
            print('enter the ',i+1,'number: ')
            self.userlist[i] = int(input())
        return self.userlist

    def is_list_equal(self):
        for i in range (self.gamedifficulty):
            if (self.userlist[i] != self.valuesdict[i]):
                return  0
            else:
                return  1


    def play(self,gamedifficulty):
        self.gamedifficulty = int(gamedifficulty)
        self.secretlist = MemoryGame.generate_sequence(self)
        self.guess = MemoryGame.get_list_from_user(self)
        self.result = MemoryGame.is_list_equal(self)
        return self.result



