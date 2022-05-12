def solution(entrances, exits, path):
    res = [ 0 ] * (len(path) - len(entrances) )

    for destination in range( len(entrances), len(path[0]), 1 ):

        for room in range(len(path)):

            res[destination - len(entrances)] += path[room][destination]

    return min(res)*len(exits)