#from sportsipy.ncaab.teams import Teams
#from sportsipy.ncaab.player import Player
#import MarchMadness


#Accept a plus minus bet
def plusMinus(team, amt):
    return

#Accept a money line bet
def moneyLine(team, amt):
    return

#Accept a over/under bet
def overUnder(choice, amt):
    return

#Accept a bet on player points
#Bets are made on an over/under line for predicted player points
def playerPoints(player, amt):
    return

#Accept a bet on player assists
#Similar to points bet
def playerAssits(player, choice, amt):
    return

#Bet which team scores first
def firstBasket(team, amt):
    return

#Bet which team wins the tip
def tipOff(team, amt):
    return

#Bet if game goes into OT
def overtime(choice, amt):
    return

#Bet on color of coaches shoes
def coachShoes(choice, amt):
    return

#Set up basic command line interface
def userInterface():
    print(
        '''
    1. Plus/Minus bet 
    2. Money Line bet 
    3. Over/Under bet 
    4. Player points prop bet
    5. Player assists prop bet
    6. First basket prop bet
    7. Tipoff prop bet
    8. Overtime bet
    9. Coach shoes prop bet
    '''
    )
    choice = input("Choose which bet you want to make (number by bet): ")


userInterface()