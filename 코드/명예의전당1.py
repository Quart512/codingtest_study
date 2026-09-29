import heapq


def solution(k, score):
    answer = []
    hlist = []
    for s in score:
        heapq.heappush(hlist, s)
        if len(hlist) > k:
            heapq.heappop(hlist)
        answer.append(hlist[0])
    return answer


TESTS = [
    (3, [10, 100, 20, 150, 1, 100, 200], [10, 10, 10, 20, 20, 100, 100]),
    (4, [0, 300, 40, 300, 20, 70, 150, 50, 500], [0, 0, 0, 0, 20, 40, 70, 70, 150]),
    (1, [5, 3, 9, 1], [5, 5, 9, 9]),
    (5, [7, 7, 7], [7, 7, 7]),
]


if __name__ == "__main__":
    for k, score, expected in TESTS:
        got = solution(k, score[:])
        assert got == expected, f"k={k}, {score} -> {got}, 기대값 {expected}"
    print("통과")
