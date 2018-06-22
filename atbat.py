import settings
import random as rn


def atBat(pitcher, batter):
    """ Function to complete an at bat and output result"""
    """ return: [out, hit, extra base, runners advance, bb, mss]"""
    print('\n')
    print('Pitcher: %s' % (settings.cname(pitcher)))
    print('Now batting: %s' % (settings.cname(batter)))
    print('BT: %i, WT: %i' % (batter.bt, batter.wt))
    batter.pa += 1
    ss = rn.randint(1, 100)
    if pitcher.pitchDie > 0:
        pd = rn.randint(1, pitcher.pitchDie)
    elif pitcher.pitchDie < 0:
        pd = rn.randint(pitcher.pitchDie, -1)
    mss = ss + pd
    print('MSS: %i' % mss)
    if mss <= batter.bt:
        hd = rn.randint(1, 20)
        print('hd: %s' % hd)
        if settings.hitTable[hd][1] != 'N/A':
            dd = rn.randint(1, 12)
            print('dd: %s' % dd)
            if dd == 12:
                batter.ab += 1
                print('Result: Out!')
                return [1, 0, 0, 0, 0, mss, batter]
            elif dd in [10, 11]:
                hr = settings.hitTable[hd][0]
                hra = settings.hitTable[hd][0] - 1
                if hra == 0:
                    hra = 1
                ra = hr
                res = settings.resultTable[hra]
                print(('Result: %s, with great defense! ' +
                       'Runners advance %i base(s).') % (res, ra))
                batter.ab += 1
                batter.hits += 1
                if hra == 2:
                    batter.hh += 1
                elif hra == 3:
                    batter.hhh += 1
                elif hra == 4:
                    batter.hr += 1
                return [0, hra, 0, ra, 0, mss, batter]
            elif dd >= 3 and dd <= 9:
                hr = settings.resultTable[settings.hitTable[hd][0]]
                ra = settings.hitTable[hd][2]
                batter.ab += 1
                batter.hits += 1
                if hr == 2:
                    batter.hh += 1
                elif hr == 3:
                    batter.hhh += 1
                elif hr == 4:
                    batter.hr += 1
                print('Result: %s! Runners advance %i base(s).'
                      % (hr, ra))
                return [0, settings.hitTable[hd][0], 0, ra, 0, mss, batter]
            elif dd < 3:
                hr = (settings.resultTable[settings.hitTable[hd][0] +
                      settings.defTable[dd][1]])
                ra = settings.hitTable[hd][2] + settings.defTable[dd][2]
                batter.ab += 1
                batter.hits += 1
                if settings.hitTable[hd][0] == 2:
                    batter.hh += 1
                elif settings.hitTable[hd][0] == 3:
                    batter.hhh += 1
                elif settings.hitTable[hd][0] == 4:
                    batter.hr += 1
                print('Result: %s and an error! Runners advance %i base(s).'
                      % (hr, ra))
                return [0, settings.hitTable[hd][0], 1, ra, 0, mss, batter]
        elif settings.hitTable[hd][1] == 'N/A':
            hr = settings.resultTable[settings.hitTable[hd][0]]
            ra = settings.hitTable[hd][2]
            batter.ab += 1
            if hr == 2:
                batter.hh += 1
            elif hr == 3:
                batter.hhh += 1
            elif hr == 4:
                batter.hr += 1
            print('Result: %s! Runners advance %i base(s).'
                  % (hr, ra))
            return [0, settings.hitTable[hd][0], 0, ra, 0, mss, batter]
    elif mss > batter.bt and mss <= batter.wt:
        print("Result: Walk!")
        batter.bb += 1
        return [0, 'bb', 0, 1, 1, mss, batter]
    elif mss > batter.wt:
        ot = settings.outTable[abs(mss) % 10]
        batter.ab += 1
        if ot in (["K", "k"]):
            batter.k += 1
        print("Out! %s" % ot)
        return [1, 0, 0, 0, 0, mss, batter]
