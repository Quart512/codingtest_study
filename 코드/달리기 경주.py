def solution(players, callings):
    rank = {p: i for i, p in enumerate(players)}   # 이름 -> 인덱스
    for c in callings:
        i = rank[c]
        front = players[i-1]                       # 앞 선수: O(1)
        players[i-1], players[i] = players[i], players[i-1]
        rank[c], rank[front] = i-1, i              # 딕셔너리도 같이 갱신
    return players
