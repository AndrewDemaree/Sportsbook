from sportsipy.ncaab.teams import Teams


Team = Teams()

#D1 Averages
#Tempo: 67.3
#Off Efficiency: 103.8

#input for the team names
#team name inputs in all caps, "-" replaces spaces
"""
input1 = input('Team 1: ') 
input2 = input('Team 2: ')
#set input to teams
Team1 = Team(input1)
Team2 = Team(input2)
"""
#calculate tempo average
def tempo(Team):
    tempo = (Team.field_goal_attempts) + (.475*Team.free_throw_attempts) - (Team.offensive_rebounds) + (Team.turnovers)
    tempo = tempo/Team.games_played
    return tempo
#calculate opponents tempo average
def oppTempo(Team):
    tempo = (Team.opp_field_goals) + (.475*Team.opp_free_throw_attempts) - (Team.opp_offensive_rebounds) + (Team.opp_turnovers) 
    tempo = tempo/Team.games_played
    return tempo
#calculate off efficiency
def offensiveEfficiency(Team):
    efficiency = ((Team.points / Team.games_played) / tempo(Team)) * 100
    return efficiency

#calculate def efficiency
def defensiveEfficiency(Team):
    efficiency = ((Team.opp_points / Team.games_played) / tempo(Team)) * 100
    return efficiency
#adjusted tempo
def adjustTempo(Team1, Team2):
    tempAvg = 67.3
    adjustTemp = tempAvg - (tempAvg - tempo(Team1)) - (tempAvg - tempo(Team2))
    return adjustTemp
#adjusted off efficiency
def adjustOffEfficiency(Team, Team2):
    effAvg = 103.8
    oppDefEff = defensiveEfficiency(Team2)
    teamEff = offensiveEfficiency(Team)
    adjEff = effAvg + (teamEff - effAvg) + (oppDefEff - effAvg)
    return adjEff
#variable adjustment for team
def teamVariable(Team, Team2):
    pointVariable = 0
    #add points depending on schedule strength
    if Team.simple_rating_system > Team2.simple_rating_system:
        pointVariable += .5
    if Team.strength_of_schedule > Team2.strength_of_schedule:
        pointVariable += .5
        if (Team.strength_of_schedule - Team2.strength_of_schedule) > 15: #add more if far greater schedule
            pointVariable += 1.5
    #add points based on better rebounding team
    if Team.total_rebound_percentage > Team2.total_rebound_percentage:
        pointVariable += .5
    #add points based on better TS% team
    if Team.true_shooting_percentage > Team2.true_shooting_percentage:
        pointVariable += .5
    return pointVariable
#predict the score
def predictScore(Team1, Team2):
    adjustedTemp = adjustTempo(Team1, Team2)
    Score1 = (adjustOffEfficiency(Team1, Team2)/100) * adjustedTemp
    Score2 = (adjustOffEfficiency(Team2, Team1)/100) * adjustedTemp
    Score1 += teamVariable(Team1, Team2)
    Score2 += teamVariable(Team2, Team1)

    print(Team1.abbreviation + ":", Score1)
    print(Team2.abbreviation + ":", Score2)


"""
print()
print(input1 ,'off efficiency: ', offensiveEfficiency(Team1))
print(input1, 'def efficienty: ', defensiveEfficiency(Team1))
print(input1, 'tempo: ', tempo(Team1))
print(input1, 'adj off efficiency', adjustOffEfficiency(Team1, Team2))
print()
print(input2 ,'off efficiency: ', offensiveEfficiency(Team2))
print(input2, 'def efficienty: ',defensiveEfficiency(Team2))
print(input2, 'tempo: ',tempo(Team2))
print(input2, 'adj off efficiency', adjustOffEfficiency(Team2, Team1))
print()
print('adjust tempo: ', adjustTempo(Team1,Team2))
print()
predictScore(Team1, Team2)
"""
