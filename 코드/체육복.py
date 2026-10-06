def solution(n, lost, reserve):
    answer = 0
    lost.sort()

    solved=[]
    for r in reserve:
        if r in lost:
            solved.append(r)
    for s in solved:
        lost.remove(s)
        reserve.remove(s)
    solved=[]
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            solved.append(l)
        elif l in reserve:
            reserve.remove(l)
            solved.append(l)
        elif l+1 in reserve:
            reserve.remove(l+1)
            solved.append(l)
    answer=n-len(lost)+len(solved)
    return answer


TESTS = [
    # 공식 예제
    (5, [2, 4], [1, 3, 5], 5),
    (5, [2, 4], [3], 4),
    (3, [3], [1], 2),
    # 도난당했는데 여벌도 있는 학생은 빌려줄 수 없다
    (3, [1, 2], [2, 3], 2),
    (3, [2, 3], [1, 2], 2),
    (2, [1, 2], [2], 1),
    # 정렬되지 않은 입력
    (5, [3, 1], [4, 2], 5),
]


if __name__ == "__main__":
    for n, lost, reserve, expected in TESTS:
        got = solution(n, lost[:], reserve[:])
        assert got == expected, f"{(n, lost, reserve)} -> {got}, 기대값 {expected}"
    print("통과")
