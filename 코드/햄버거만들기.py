def solution(ingredient):
    answer = 0
    stack=[]
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4:
            if stack[-1]==1:
                if stack[-2]==3:
                    if stack[-3]==2:
                        if stack[-4]==1:
                            answer+=1
                            for _ in range(4):
                                stack.pop()
    return answer


TESTS = [
    # 공식 예제
    ([2, 1, 1, 2, 3, 1, 2, 3, 1], 2),
    ([1, 3, 2, 1, 2, 1, 3, 1, 2], 0),
    # 재료가 4개보다 적을 때
    ([1, 2, 3], 0),
    ([1, 2, 3, 1], 1),
    # 마지막 빵은 다음 햄버거의 첫 빵으로 다시 쓸 수 없다
    ([1, 2, 3, 1, 2, 3, 1], 1),
    # 하나를 포장하고 나면 그 위아래가 붙어서 새 햄버거가 된다
    ([1, 2, 1, 2, 3, 1, 3, 1], 2),
]


if __name__ == "__main__":
    for ingredient, expected in TESTS:
        got = solution(ingredient[:])
        assert got == expected, f"{ingredient} -> {got}, 기대값 {expected}"
    print("통과")
