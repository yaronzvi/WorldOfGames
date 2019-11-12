class WorldOfGames:

# 10.11.2019 by yaron zvi - devops course

#This function has a person name as an input and returns a string in the following layout:
    def welcome(name):
        print ('Hello '+name+' and welcome to the World of Games (WoG).')
        print('Here you can find many cool games to play.')
        WorldOfGames.name = name

#This function prints out the following text:
    def load_game():
        option = [1, 2, 3]
        difficulty = [1, 2, 3, 4, 5]
        print('Please choose a game to play:')
        print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
        print('2. Guess Game - guess a number and see if you chose like the computer')
        print('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
        gameoption = float(input())


        if (gameoption not in option):
            print('you didnt enter option 1 2 or  3 please try again')
            return
        else:
            print('Please choose game difficulty from 1 to 5:')
            gamedifficulty = float(input())

        if (gamedifficulty not in difficulty ):
                print('you didnt enter difficulty 1 to 5 please try again ')
                return
        else:
               print(gameoption, gamedifficulty)


