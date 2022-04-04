
from sportsipy.ncaab.teams import Teams
from sportsipy.ncaab.roster import Player
from sportsipy.ncaab.roster import Roster
import MarchMadness
import numpy
import random

txtFile = open('Bets.txt','w')



#Accept a plus minus bet
def plusMinus():
    teams = Teams()
    userchoice = input('Choose a Team (Kansas or North-Carolina): ').upper()

    for team in teams:
        if team.abbreviation == userchoice:
            if userchoice == "KANSAS":
                prefix = "-"
            if userchoice == "NORTH-CAROLINA":
                prefix = "+"
            pointsdiffential = team.points - team.opp_points
            projectedwinningpercentage = round((100 - ((pointsdiffential * 2.7) + 41) / 82))
            odds = prefix + str(100 + projectedwinningpercentage)
            bet = input(
                "The odds are " + odds + " , enter bet amount in multiples of one-hundred, plus " + odds[1:] + ":")

            if prefix == "+":
                add = (int(odds[1:]) - 100)
                factor = (int(bet) - add) / 100
                winnings = factor * 100 + add * factor
                print("Winnings: " + str(winnings))
                # txtFile.write('Bet $' + str(bet) + ' plus/minus to win $' + str(winnings) + '\n')
            if prefix == "-":
                print((int(bet) - projectedwinningpercentage) / 10)
                winnings = ((int(bet) - projectedwinningpercentage) / 10) * projectedwinningpercentage
                print("Winnings: " + str(winnings))
                txtFile.write('Bet $' + str(bet) + ' plus/minus to win $' + str(winnings) + '\n')
            
            userInterface()

#Accept a money line bet
def moneyLine():
    return

#Accept a over/under bet
def overUnder():
    score1 = scores[0]
    score2 = scores[1]
    line1=-100
    line2=-100

    if (score1 > score2):
        sDiff = score1 - score2
        line1 = 100
        line2 = -100
        line1+= sDiff * 40
        line2+= -(sDiff * 40)
    else:
        sDiff = score2 - score1
        line1 = -100
        line2 = 100
        line1+= -(sDiff * 40) - 10
        line2+= sDiff * 40 + 10

    lines=[]
    lines.append(line1)
    lines.append(line2)
    return lines

#Accept a bet on player points
#Bets are made on an over/under line for predicted player points
def playerPoints(amt):
    kansasPlayers = ['ochai-agbaji-1','christian-braun-1','jalen-wilson-1','david-mccormack-1','remy-martin-2','dajuan-harris-1']
    uncPlayers = ['armando-bacot-1','caleb-love-1','brady-manek-1','rj-davis-1','rechon-black-1','dawson-garcia-1']
    
    betAmt = amt
    #Get player that user wants to bet on
    team = input('Choose a Team (KANSAS or NORTH-CAROLINA): ')
    if team == 'KANSAS':
        print(
        '''
    1. Ochai Agbaji 
    2. Christian Braun 
    3. Jalen Wilson 
    4. David McCormack
    5. Remy Martin
    6. Dajuan Harris
    '''
    )
    #Find player points average
        player = input('Choose player by number: ')
        player = kansasPlayers[int(player) - 1]
        
        playerAvg = Player(player).points_produced/Player(player).games_played
        playerAvg = round(playerAvg)
        #set line to average plus .5 points
        pointLine = float(playerAvg) + .5
        input2 = input('Line set at ' +  str(pointLine) +  ' points. Do you want to bet the over or under? (o or u): ' )

        underOdds = -180
        overOdds = +220


        if input2 == 'u' or input2 == 'U':
            betType = 'under'
            winnings  =  amt + (amt * ((-1 * underOdds) / 100))
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(pointLine)+' points bet to win $' + str(winnings)+ '\n')
        if input2 == 'o' or input2 == 'O':
            betType = 'over'
            winnings = amt + ((amt*overOdds) / 100)
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(pointLine)+' points bet to win $' + str(winnings)+ '\n')
        
        userInterface()


    if team == "NORTH-CAROLINA":
        print(
        '''
    1. Armando Bacot
    2. Caleb Love 
    3. Brady Manek 
    4. RJ Davis
    5. Leaky Black
    6. Dawson Garcia
    ''' 
    )
        player = input('Choose player by number: ')
        player = uncPlayers[int(player) - 1]
        playerAvg = Player(player).points_produced/Player(player).games_played
        playerAvg = round(playerAvg)
        #set line to average plus .5 points
        pointLine = float(playerAvg) + .5
        input2 = input('Line set at ' +  str(pointLine) +  ' points. Do you want to bet the over or under? (o or u): ' )

        underOdds = -180
        overOdds = +220
        if input2 == 'u' or input2 == 'U':
            betType = 'under'
            winnings  =  amt + (amt * ((-1 * underOdds) / 100))
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(pointLine)+' points bet to win $' + str(winnings)+ '\n')
        if input2 == 'o' or input2 == 'O':
            betType = 'over'
            winnings = amt + ((amt*overOdds) / 100)
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(pointLine)+' points bet to win $' + str(winnings)+ '\n')

        userInterface()
        

    

#Accept a bet on player assists
#Similar to points bet
def playerAssists(amt):
    kansasPlayers = ['ochai-agbaji-i','christian-braun-1','jalen-wilson-1','david-mccormack-1','remy-martin-2','dajuan-harris-1']
    uncPlayers = ['armando-bacot-1','caleb-love-1','brady-manek-1','rj-davis-1','rechon-black-1','dawson-garcia-1']
    
    betAmt = amt
    #Get player that user wants to bet on
    team = input('Choose a Team (KANSAS or NORTH-CAROLINA): ')
    if team == 'KANSAS':
        print(
        '''
    1. Ochai Agbaji 
    2. Christian Braun 
    3. Jalen Wilson 
    4. David McCormack
    5. Remy Martin
    6. Dajuan Harris
    '''
    )
    #Find player points average
        player = input('Choose player by number: ')
        player = kansasPlayers[int(player) - 1]
        
        playerAvg = Player(player).assists/Player(player).games_played
        playerAvg = round(playerAvg)
        #set line to average plus .5 assists
        assistLine = float(playerAvg) + .5
        input2 = input('Line set at ' +  str(assistLine) +  ' assists. Do you want to bet the over or under? (o or u): ' )
        print()

        underOdds = -120
        overOdds = +140


        if input2 == 'u' or input2 == 'U':
            betType = 'under'
            winnings  =  amt + (amt * ((-1 * underOdds) / 100))
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(assistLine)+' assists bet to win $' + str(winnings)+ '\n')

        if input2 == 'o' or input2 == 'O':
            betType = 'over'
            winnings = amt + ((amt*overOdds) / 100)
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(assistLine)+' assists bet to win $' + str(winnings)+ '\n')


        userInterface()


    if team == "NORTH-CAROLINA":
        print(
        '''
    1. Armando Bacot
    2. Caleb Love 
    3. Brady Manek 
    4. RJ Davis
    5. Leaky Black
    6. Dawson Garcia
    ''' 
    )
        player = input('Choose player by number: ')
        player = uncPlayers[int(player) - 1]
        playerAvg = Player(player).assists/Player(player).games_played
        playerAvg = round(playerAvg)
        #set line to average plus .5 assists
        assistLine = float(playerAvg) + .5
        input2 = input('Line set at ' +  str(assistLine) +  ' assists. Do you want to bet the over or under? (o or u): ' )
        print()

        underOdds = -100
        overOdds = +100
        if input2 == 'u' or input2 == 'U':
            betType = 'under'
            winnings  =  amt + (amt * ((-1 * underOdds) / 100))
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(assistLine)+' assists bet to win $' + str(winnings)+ '\n')

        if input2 == 'o' or input2 == 'O':
            betType = 'over'
            winnings = amt + ((amt*overOdds) / 100)
            txtFile.write('Bet $' + str(amt) + ' on '+ Player(player).name + ' '+ betType + ' '+ str(assistLine)+' assists bet to win $' + str(winnings)+ '\n')

        
        userInterface()

#Bet which team scores first
def firstBasket():
    team = 'UNC'
    opponent = 'you lost'
    userchoice = input("Enter Team name:")
    amt = int(input('Enter bet:'))
    tip_win = random.choice([team, opponent])
    first_basket = numpy.random.choice([team, opponent], p=[.60, .40])
    team_pts_avg = 79 # Kansas
    opponent_pts_avg = 78 #UNC
    add_avg = team_pts_avg + opponent_pts_avg
    diff = team_pts_avg - opponent_pts_avg
    added = diff * 10
    if team_pts_avg > opponent_pts_avg:
        odds = -100 - added
    else:
        added = abs(added)
        odds = 100 + added
    if odds < 0:
        amount = amt + (amt * ((-1 * odds) / 100))
    else:
        amount = amt + ((amt * odds) / 100)
    teams = [team, opponent]
    if first_basket == team:
        winner = amount
        txtFile.write('Bet $' + str(amt) + ' on which team scores first to win $' + str(amount) + '\n')
    else:
        winner = opponent
        txtFile.write('You Bet $' + str(amt) + '\n')
    userInterface()
    return winner
    

#Bet which team wins the tip
def tipOff():
    team = 'UNC'
    userchoice = input("Enter Team name:")
    amt = int(input('Enter bet:'))
    opponent = 'You lost'
    player1_h = 84 #Kansas Udoka height in inches
    player2_h = 82 # UNC Bacot
    add_h = player1_h + player2_h
    dif = player1_h - player2_h
    added = dif * 10
    if player1_h > player2_h:
        odds = -100 - added
    else:
        added = abs(added)
        odds = 100 + added
    if odds < 0:
        amount = amt + (amt * ((-1 * odds) / 100))
    else:
        amount = amt + ((amt * odds) / 100)
    teams = [team, opponent]
    weight1 = player1_h / add_h
    weight2 = player2_h / add_h
    tipoff = numpy.random.choice(teams, p = [weight1, weight2])
    if tipoff == team:
        winner = amount
        txtFile.write('Bet $' + str(amt) + ' on which team wins the tip off to win $' + str(amount) + '\n')
    else:
        winner = opponent
        txtFile.write('You Bet $' + str(amt) + '\n')
    userInterface()
    return winner


#Bet if game goes into OT
def overtime():
    score1 = scores[0]
    score2 = scores[1]

    if (score1 > score2):
        sDiff = score1 - score2
    else:
        sDiff = score2 - score1
    
    line1 = 300
    line1 += sDiff * 40

    lines=[]
    lines.append(line1)
    print(lines)
    return lines

#Bet on color of coaches shoes
def coachShoes():
    teams = ["KANSAS", "UNC"]
    colors = ["BLUE", "BLACK", "WHITE"]
    odds = [[[0.1], [0.1], [0.8]], [[0.8], [0.1], [0.1]]]
    usrchoice = input("Enter Team name (UNC or Kansas):").upper()
    shoecolor = input("Enter shoe color (blue, black, or white):").upper()
    amt = input("Enter bet amount:")

    for team in teams:
        if team == usrchoice:
            first = teams.index(str(team))
            break

    for color in colors:
        if color == shoecolor.upper():
            odd = odds[first][colors.index(str(color))][0]
            winnings = int(amt) * odd + int(amt)
            payout = "$" + str(winnings)
            print('Winnings: ' + payout)
            txtFile.write('Bet $' + str(amt) + ' to win $' + str(winnings) + ' on shoe color ' + str(color) + '\n')
            userInterface()
            break

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
    choice = input("Choose which bet you want to make (number by bet) or type e to exit: ")
    if choice == 'e' or choice == 'E':
        print('Your bets are saved to Bets.txt \n')
        print('Thanks for betting!')
        exit()
    
    if choice == '1':
        plusMinus()
    if choice == '2':
        moneyLine()
    if choice == '3':
        overUnder()
    if choice == '4':
        money = input("Choose how much you want to bet: ")
        betAmt = int(money)
        playerPoints(betAmt)
    if choice == '5':
        money = input("Choose how much you want to bet: ")
        betAmt = int(money)
        playerAssists(betAmt)
    if choice == '6':
        firstBasket()
    if choice == '7':
        tipOff()
    if choice == '8':
        overtime()
    if choice == '9':
        coachShoes()
    


userInterface()
