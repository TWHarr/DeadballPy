import names
import random as rn


def getKey(custom):
    return custom.bt


class Starter(object):
    """Create a new starter"""
    def __init__(self, pos):
        self.name = newName()
        self.hand = newHand()
        self.pos = pos
        self.bt = rn.randint(2, 20) + 15
        self.wt = self.bt + rn.randint(2, 12)
        self.bonus = newStarterBonus()
        self.age = rn.choice([18, 21, 26, 34]) + rn.randint(1, 6)
        self.bb = 0
        self.hits = 0
        self.runs = 0
        self.rbi = 0
        self.hh = 0
        self.hhh = 0
        self.hr = 0
        self.k = 0
        self.pa = 0
        self.ab = 0
        self.SAC = 0
        self.first = False
        self.second = False
        self.third = False

    def __repr__(self):
        return('%s, %s. %i/%i%s %s' % (cname(self), self.pos,
                                       self.bt, self.wt,
                                       self.hand, self.bonus))


class Pinch(object):
    """Create a pinch player"""
    def __init__(self, pos):
        self.name = newName()
        self.hand = newHand()
        self.pos = pos
        self.bt = rn.randint(1, 10) + 15
        self.wt = self.bt + rn.randint(2, 12)
        self.bonus = newPinchBonus()
        self.age = rn.choice([18, 21, 26, 34]) + rn.randint(1, 6)
        self.bb = 0
        self.hits = 0
        self.runs = 0
        self.rbi = 0
        self.hh = 0
        self.hhh = 0
        self.hr = 0
        self.k = 0
        self.pa = 0
        self.ab = 0
        self.SAC = 0
        self.first = False
        self.second = False
        self.third = False

    def __repr__(self):
        return('%s, %s. %i/%i%s %s' % (cname(self), self.pos,
                                       self.bt, self.wt,
                                       self.hand, self.bonus))


class Pitcher(object):
    """Create a pitcher"""
    def __init__(self, pos):
        self.name = newName()
        self.hand = rn.choice(['R', 'R', 'R', 'L'])
        self.pos = pos
        self.bt = rn.randint(1, 10) + 5
        self.wt = self.bt + rn.randint(2, 12)
        self.bonus = newPitcherBonus()
        self.age = rn.choice([18, 21, 26, 34]) + rn.randint(1, 6)
        self.pitchDie = rn.choice([12, 8, 8, 4, 4, 4, -4, -4])
        self.bb = 0
        self.hits = 0
        self.runs = 0
        self.rbi = 0
        self.hh = 0
        self.hhh = 0
        self.hr = 0
        self.k = 0
        self.pa = 0
        self.ab = 0
        self.SAC = 0
        self.first = False
        self.second = False
        self.third = False
        self.BF = 0
        self.SO = 0
        self.BBA = 0
        self.hitA = 0
        self.ER = 0
        self.R = 0

    def __repr__(self):
        return('%s, %s. %i/%i%s %s' % (cname(self), self.pos,
                                       self.bt, self.wt,
                                       self.hand, self.bonus))


class Team(object):
    """Create a team object."""

    def __init__(self, name):
        self.name = name
        self.players = self.generatePlayers()
        self.lineup = self.generateLineup(self.players)

    def generatePlayers(self):
        players = []
        for position in positions:
            a = createPlayer(position)
            players.append(a)
        return players

    def generateLineup(self, players):
        batters = players[0:8]
        sp = []
        a = sorted(batters, key=getKey, reverse=True)
        for player in players:
            if player.pos == 'SP':
                sp.append(player)
        a.append(rn.choice(sp))
        return a

    def printPlayers(self):
        for item in self.players:
            print(item)

    def printLineup(self):
        for item in self.lineup:
            print(item)

def createPlayer(pos):
    """ determine which class a player should be """
    if pos == 'RP' or pos == 'SP':
        player = Pitcher(pos)
        return player
    if pos == 'IF' or pos == 'OF' or pos == 'C2':
        player = Pinch(pos)
        return player
    else:
        player = Starter(pos)
        return player


def newName():
    """ randomly generate a new player name """
    a = rn.choice(names.firstNames)
    b = rn.choice(names.surnames)
    player = [a, b]
    return player


def newHand():
    """ choose a hand for a player """
    return rn.choice(['R', 'R', 'R', 'R', 'R', 'R', 'L', 'L', 'L', 'S'])


def newStarterBonus():
    """ determine what bonus a starter gets """
    a = rn.randint(2, 12)
    traits = {
        2: "S+, D+",
        3: "S+",
        4: "D+",
        10: "P+",
        11: "C+",
        12: "P++"
    }
    if a in traits:
        return traits[a]
    else:
        return ''


def newPinchBonus():
    """ determine which bonus a pinch hitter gets """
    a = rn.randint(2, 12)
    traits = {
        2: "S+",
        3: "C+",
        11: "D+",
        12: "P+"
    }
    if a in traits:
        return traits[a]
    else:
        return ''


def newPitcherBonus():
    """ determine which bonus a pitcher gets """
    a = rn.randint(2, 12)
    traits = {
        2: "GB+",
        3: "K+",
        11: "ST+",
        12: "CN+"
    }
    if a in traits:
        return traits[a]
    else:
        return ''


def cname(names):
    """ structure names for printing """
    return (names.name[0] + ' ' + names.name[1]).title()


def selectTeams():
    """ select two teams for a game """
    a = rn.choice(teamNames)
    b = rn.choice(teamNames)
    while b == a:
        b = rn.choice(teamNames)
    return Team(a), Team(b)

#[bases for hitter, desc, bases for runners]
hitTable = {
    1: [1, 'N/A', 1],
    2: [1, 'N/A', 1],
    3: [1, '1B', 1],
    4: [1, '2B', 1],
    5: [1, '3B', 1],
    6: [1, 'SS', 1],
    7: [1, rn.choice(['3B', 'SS']), 1],
    8: [1, 'N/A', 2],
    9: [1, 'N/A', 2],
    10: [1, 'N/A', 2],
    11: [1, 'N/A', 2],
    12: [1, 'N/A', 2],
    13: [2, 'LF', 2],
    14: [2, 'CF', 2],
    15: [2, 'RF', 2],
    16: [2, 'N/A', 3],
    17: [2, 'N/A', 3],
    18: [3, rn.choice(['RF', 'CF']), 3],
    19: [4, 'N/A', 4],
    20: [4, 'N/A', 4]
}

defTable = {
    1: ['Error', 1, 1],
    2: ['Error', 1, 1],
    3: ['N/A', 0, 0],
    4: ['N/A', 0, 0],
    5: ['N/A', 0, 0],
    6: ['N/A', 0, 0],
    7: ['N/A', 0, 0],
    8: ['N/A', 0, 0],
    9: ['N/A', 0, 0],
    10: ['Good Defense', -1, -1],
    11: ['Good Defense', -1, -1],
    12: ['Out', 0, 0]
}

resultTable = {
    1: 'Single',
    2: 'Double',
    3: 'Triple',
    4: 'Home Run'
}

outTable = {
    0: 'K',
    1: 'k',
    2: 'k',
    3: 'U3',
    4: '4-3',
    5: '5-3',
    6: '6-3',
    7: 'F7',
    8: 'F8',
    9: 'F9'
}

teamNames = ['Broad Street Peacocks', 'Charlottesville Flycatchers',
             'Paducah Red Birds', 'Tallahassee Wrens', 'Gettysburg Owls',
             'Williamsburg Ospreys', 'Cooper River Chickadees',
             'Knoxville Grackles']

positions = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'IF', 'IF', 'OF',
             'OF', 'C2', 'SP', 'SP', 'SP', 'SP', 'SP', 'RP', 'RP', 'RP', 'RP',
             'RP', 'RP', 'RP']


def startingLineups(team):
    print("\nStarting lineup for the %s:" % team.name)
    for player, value in enumerate(team.lineup, 1):
        print(player, value)
