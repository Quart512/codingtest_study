def solution(players, callings):
    rank = {p: i for i, p in enumerate(players)}
    for c in callings:
        i = rank[c]
        front = players[i-1]
        players[i-1], players[i] = players[i], players[i-1]
        rank[c], rank[front] = i-1, i
    return players


TESTS = [
    (["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"], ["mumu", "kai", "mine", "soe", "poe"]),
    (["a", "b"], ["b"], ["b", "a"]),
    (["a", "b", "c"], ["c", "c"], ["c", "a", "b"]),
    (["a", "b", "c"], [], ["a", "b", "c"]),
]


if __name__ == "__main__":
    for players, callings, expected in TESTS:
        got = solution(players[:], callings[:])
        assert got == expected, f"{(players, callings)} -> {got}, 기대값 {expected}"
    # 문제 최대 입력(선수 5만, 부름 100만)에서 시간 초과가 안 나는지
    import random, time
    random.seed(0)
    players = [f"p{i}" for i in range(50000)]
    cur, callings = players[:], []
    for _ in range(1000000):
        i = random.randint(1, len(cur) - 1)
        callings.append(cur[i])
        cur[i-1], cur[i] = cur[i], cur[i-1]
    t = time.time()
    got = solution(players[:], callings)
    assert got == cur
    print(f"통과 (선수 5만, 부름 100만: {time.time() - t:.3f}s)")
