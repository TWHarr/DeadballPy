import atbat as ab
import settings

def process(a, state, battingTeam):
    """ return: [out, hit, extra base, runners advance, bb, mss, batter]"""
    if a[0] == 1:
        if a[5] > 70 and settings.outTable[abs(a[5]) % 10] >= 7:
            pass
        if a[5] > 70 and 3 <= settings.outTable[abs(a[5]) % 10] <= 6:
            if state.bases == {'First': 1, 'Second': 0, 'Third': 0}:
                pass
            elif state.bases == {'First': 0, 'Second': 1, 'Third': 0}:
                state.bases = {'First': 0, 'Second': 0, 'Third': 1}
            elif state.bases == {'First': 0, 'Second': 0, 'Third': 1}:
                state.bases = {'First': 0, 'Second': 0, 'Third': 0}
                score.battingTeam += 1
            elif state.bases == {'First': 1, 'Second': 1, 'Third': 0}:
                state.bases = {'First': 1, 'Second': 0, 'Third': 1}
            elif state.bases == {'First': 1, 'Second': 0, 'Third':1}:
                state.bases = {'First': 1, 'Second': 0, 'Third': 0}
                score.battingTeam += 1

        elif a[5] <= 70 and settings.outTable[abs(mss) % 10] >= 7 :
            pass
        elif a[5] <= 70 and 3 <= settings.outTable[abs(a[5]) % 10] <= 6:
            pass
    elif a[0] == 0:
        if a[1] == 'bb':

        else:


def inning(inningNumber, awayLineup, awayBatter, homeLineup, homeBatter):

    score = settings.Score()
    awayState = settings.BaseState()
    homeState = settings.BaseState()

    print("\nTop of Inning %s ++++++++++++++++++++++++++" % inningNumber)
    awayBatter = awayBatter
    awayOuts = 0
    while awayOuts < 3:
        a = ab.atBat(homeLineup[8], awayLineup[awayBatter])
        awayBatter += 1
        if awayBatter == 9:
            awayBatter = 0
        awayOuts += a[0]
        print("%s outs" % (awayOuts))

    print("\nBottom of Inning %s +++++++++++++++++++++++" % inningNumber)
    homeBatter = homeBatter
    homeOuts = 0
    while homeOuts < 3:
        a = ab.atBat(awayLineup[8], homeLineup[homeBatter])
        homeBatter += 1
        if homeBatter == 9:
            homeBatter = 0
        homeOuts += a[0]
        print("%s outs" % (homeOuts))
    print("==================================================================")
