def solution(elements):
    answer = 0
    aset=set()
    aset.update(elements)
    length=len(elements)
    elements=elements*2
    for i in range(length-1):
        for l in range(length):
            aset.add(sum(elements[l:l+i+2]))
    answer=len(aset)
    return answer


TESTS = [
    # 공식 예제
    ([7, 9, 1, 1, 4], 18),
    # 원형: 3 + 1 처럼 끝과 처음이 이어진 수열도 센다
    ([1, 2, 3], 6),
    # 같은 합은 한 번만
    ([1, 1, 1], 3),
    ([5, 5, 5, 5], 4),
]


if __name__ == "__main__":
    for elements, expected in TESTS:
        got = solution(elements[:])
        assert got == expected, f"{elements} -> {got}, 기대값 {expected}"
    print("통과")
