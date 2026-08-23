def solution(cards1, cards2, goal):
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


TESTS = [
    (["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"], "Yes"),
    (["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"], "No"),
    (["a"], ["b"], ["a", "b", "c"], "No"),
    (["a", "b"], ["c"], ["a", "b", "c"], "Yes"),
]


if __name__ == "__main__":
    for cards1, cards2, goal, expected in TESTS:
        got = solution(cards1[:], cards2[:], goal[:])
        assert got == expected, f"{(cards1, cards2, goal)} -> {got}, 기대값 {expected}"
    print("통과")
