def solution(numbers):
    answer = []
    stack =[]
    while numbers:
        while stack:
            if stack[-1]>numbers[-1]:
                answer.append(stack[-1])
                break
            else:
                stack.pop()
        else:
            answer.append(-1)
        stack.append(numbers.pop())
    answer.reverse()
    return answer


TESTS = [
    # 공식 예제
    ([2, 3, 3, 5], [3, 5, 5, -1]),
    ([9, 1, 5, 3, 6, 2], [-1, 5, 6, 6, -1, -1]),
    # 같은 숫자는 큰 수가 아니다
    ([5, 5, 5, 5], [-1, -1, -1, -1]),
    # 내림차순: 뒤에 큰 수가 하나도 없다
    ([4, 3, 2, 1], [-1, -1, -1, -1]),
    # 오름차순: 바로 뒤가 답
    ([1, 2, 3, 4], [2, 3, 4, -1]),
    # 큰 수 하나가 기다리던 숫자 여럿의 답이 된다
    ([3, 1, 2, 1, 4], [4, 2, 4, 4, -1]),
]


if __name__ == "__main__":
    for numbers, expected in TESTS:
        got = solution(numbers[:])
        assert got == expected, f"{numbers} -> {got}, 기대값 {expected}"
    print("통과")
