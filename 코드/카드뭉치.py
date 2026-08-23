"""
프로그래머스 159994 - 카드 뭉치
https://school.programmers.co.kr/learn/courses/30/lessons/159994

오답노트: ../오답노트/카드뭉치.md

같은 문제를 세 가지 방법으로 푼다. 정답 여부는 셋 다 같고, 차이는 '비용'이다.
    solution_pop      : list.pop(0)  -> 전체 O(n^2), 원본 리스트 파괴
    solution_deque    : popleft()    -> 전체 O(n),   원본 리스트 파괴(복사본 사용)
    solution_pointer  : 인덱스 이동   -> 전체 O(n),   원본 그대로 (권장)
"""

from collections import deque


def solution_pop(cards1, cards2, goal):
    """처음 제출해서 통과한 풀이.

    cards1[0] 을 먼저 쓰고 나서 cards1 이 비었는지 검사하면 IndexError 가 난다.
    파이썬 and 는 왼쪽부터 평가하므로 `cards1 and cards1[0] == goal[0]` 순서여야 안전.
    -> 에러/IndexError - list index out of range.md
    """
    answer = "Yes"
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.pop(0)
            goal.pop(0)
        elif cards2 and cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
        else:
            answer = "No"
            break
    return answer


def solution_deque(cards1, cards2, goal):
    """앞에서 빼는 연산이 진짜 병목일 때 쓰는 자료구조.

    deque.popleft() 는 O(1). 단, deque(...) 로 변환하는 데 O(n) 이 한 번 든다.
    이 문제는 카드가 최대 10장이라 체감 차이는 없다.
    """
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            return "No"
    return "Yes"


def solution_pointer(cards1, cards2, goal):
    """권장 풀이.

    '앞에서 빼는 것'처럼 보이지만 실제로는 앞에서 '읽기만' 하면 되는 문제다.
    빼지 않고 어디까지 읽었는지만 기억하면 자료구조 변환도, 원소 이동도 필요 없다.
    """
    i = j = 0
    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            return "No"
    return "Yes"


# 이름을 solution 으로 두면 그대로 제출 가능
solution = solution_pointer


TESTS = [
    (["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"], "Yes"),
    (["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"], "No"),
    # goal 을 다 만들기 전에 한쪽 뭉치가 먼저 바닥나는 경우 -> IndexError 가 났던 입력
    (["a"], ["b"], ["a", "b", "c"], "No"),
    (["a", "b"], ["c"], ["a", "b", "c"], "Yes"),
]


if __name__ == "__main__":
    for func in (solution_pop, solution_deque, solution_pointer):
        for cards1, cards2, goal, expected in TESTS:
            got = func(cards1[:], cards2[:], goal[:])  # 원본 보호를 위해 복사본 전달
            assert got == expected, f"{func.__name__}{(cards1, cards2, goal)} -> {got}, 기대값 {expected}"
        print(f"{func.__name__}: 통과")
