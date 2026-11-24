def solution(sequence, k):
    answer = []

    pointer=[0,0]
    total=sequence[0]
    while pointer!=[len(sequence),len(sequence)]:
        if total<k:
            if pointer[1]+1<len(sequence):
                total+=sequence[pointer[1]+1]
                pointer=[pointer[0],pointer[1]+1]
            else:
                break

        elif total==k:
            if answer==[] or pointer[1]-pointer[0]<answer[1]-answer[0]:
                answer=pointer
            if pointer[1]+1<len(sequence):
                total+=sequence[pointer[1]+1]
                pointer=[pointer[0],pointer[1]+1]
            else:
                break

        elif total>k:
            if pointer[0]+1<len(sequence):
                total-=sequence[pointer[0]]
                pointer=[pointer[0]+1,pointer[1]]
            else:
                break

    return answer


TESTS = [
    # 공식 예제
    ([1, 2, 3, 4, 5], 7, [2, 3]),
    ([1, 1, 1, 2, 3, 4, 5], 5, [6, 6]),
    ([2, 2, 2, 2, 2], 6, [0, 2]),
    # 길이가 같으면 앞쪽. len(answer) 로 길이를 재던 1차 제출이 [3, 3] 을 냈다
    ([3, 5, 5, 5, 6], 5, [1, 1]),
    # 첫 칸에서 바로 합이 k. 방패(answer == [])가 뒤에 있으면 IndexError
    ([5, 6, 7, 8, 9], 5, [0, 0]),
    # 답이 배열 전체. 끝을 더 늘릴 수 없을 때 멈춰야 한다
    ([1, 2, 4, 5, 5], 17, [0, 4]),
]


if __name__ == "__main__":
    for sequence, k, expected in TESTS:
        got = solution(sequence[:], k)
        assert got == expected, f"{sequence}, {k} -> {got}, 기대값 {expected}"
    print("통과")
