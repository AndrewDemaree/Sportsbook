from sportsipy.ncaab.teams import Teams

txtFile = open('Bets.txt', 'w')


# Accept a plus minus bet
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
                txtFile.write('Bet $' + str(bet) + ' plus/minus to win $' + str(winnings) + '\n')
            if prefix == "-":
                print((int(bet) - projectedwinningpercentage) / 10)
                winnings = ((int(bet) - projectedwinningpercentage) / 10) * projectedwinningpercentage
                print("Winnings: " + str(winnings))
                txtFile.write('Bet $' + str(bet) + ' plus/minus to win $' + str(winnings) + '\n')
            break


# Bet on color of coaches shoes
def coachShoes():
    teams = ["KANSAS", "UNC"]
    colors = ["BLUE", "BLACK", "WHITE"]
    odds = [[["+250"], ["+250"], ["-100"]], [["-100"], ["+250"], ["+250"]]]
    print(odds)
    usrchoice = input("Enter Team name (UNC or Kansas):").upper()
    shoecolor = input("Enter shoe color (blue, black, or white):").upper()
    amt = input("Enter bet amount in multiples of one-hundred:")
    factor = int(amt)/100

    for team in teams:
        if team == usrchoice:
            first = teams.index(str(team))
            break

    for color in colors:
        if color == shoecolor.upper():
            odd = odds[first][colors.index(str(color))][0]
            print(odd)
            if odd[0] == "+":
                winnings = int(amt) + (int(odd[1:]) * factor)
            if odd[0] == "-":
                winnings = int(amt) + (factor * 100)
            payout = "$" + str(winnings)
            print('Winnings: ' + payout)
            txtFile.write('Bet $' + str(amt) + ' to win $' + str(winnings) + ' on shoe color ' + str(color) + '\n')
            break


print(plusMinus())
print(coachShoes())
