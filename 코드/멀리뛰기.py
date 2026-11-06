def solution(n):
    one,two=1,2
    for i in range(n-1):
        one,two=two,(one+two) % 1234567
    return one


TESTS = [
    # 공식 예제
    (4, 5),
    (3, 3),
    # 작은 칸
    (1, 1),
    (2, 2),
    (5, 8),
    (6, 13),
    # 최대 입력: 나머지를 더할 때마다 구해서 숫자가 커지지 않는다
    (2000, 694725),
]


if __name__ == "__main__":
    for n, expected in TESTS:
        got = solution(n)
        assert got == expected, f"{n} -> {got}, 기대값 {expected}"
    print("통과")
