import settings
import atbat as ab
import inning as inn

print('\n\nCreating Starter')
testStarter = settings.Starter('2B')
print(testStarter)

print('\n\nCreating Pinch Hitter')
testPinch = settings.Pinch('2B')
print(testPinch)

print('\n\nCreating Pitcher')
testPitcher = settings.Pitcher('SP')
print(testPitcher)

print('\n\nCreating team a')
testTeamA = settings.Team('Test Team')
print(testTeamA.printPlayers())

print('\n\nGenerating lineup a')
testLineupA = testTeamA.generateLineup(testTeamA.players)
print(testTeamA.printLineup())

print('\n\nCreating team b')
testTeamB = settings.Team('Test Team')
print(testTeamB.printPlayers())

print('\n\nGenerating lineup b')
testLineupB = testTeamB.generateLineup(testTeamB.players)
print(testTeamB.printLineup())

settings.startingLineups(testTeamA)
settings.startingLineups(testTeamB)

for batter in testTeamA.lineup:
    ab.atBat(testTeamB.lineup[8], batter)

inn.inning(1, testTeamA.lineup, 0, testTeamB.lineup, 0)
