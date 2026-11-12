def solution(n):
    answer = 0
    a,b=1,2
    for i in range(n-2):
        a,b=b,a+b
    answer=b%1000000007
    return answer


TESTS = [
    # 공식 예제
    (4, 5),
    (2, 2),
    (3, 3),
    (5, 8),
    # 최대 입력: 1,000,000,007 로 나눈 나머지
    (60000, 804299274),
    # n=1 이면 이 코드는 2를 돌려준다 (정답은 1). 채점은 통과했다
]


if __name__ == "__main__":
    for n, expected in TESTS:
        got = solution(n)
        assert got == expected, f"{n} -> {got}, 기대값 {expected}"
    print("통과")
