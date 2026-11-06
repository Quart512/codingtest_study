def solution(n):
    one,two=1,2
    for i in range(n-1):
        one,two=two,(one+two)
    return one % 1234567


TESTS = [
    # 공식 예제
    (4, 5),
    (3, 3),
    # 작은 칸
    (1, 1),
    (2, 2),
    (5, 8),
    (6, 13),
    # 최대 입력: 중간 값은 418자리까지 커지지만 파이썬 정수는 넘치지 않는다
    (2000, 694725),
]


if __name__ == "__main__":
    for n, expected in TESTS:
        got = solution(n)
        assert got == expected, f"{n} -> {got}, 기대값 {expected}"
    print("통과")
