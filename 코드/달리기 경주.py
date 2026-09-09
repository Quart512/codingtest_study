def solution(players, callings):
    answer = []
    for calling in callings:
        called = players.index(calling)
        #players[called-1], players[called] = players[called], players[called-1]
        players.insert(called-1, players[called])
        players.pop(called+1)
    answer = players
    return answer
