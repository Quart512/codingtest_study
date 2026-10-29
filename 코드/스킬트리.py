def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        valid_skill = ""
        for s in skill_tree:
            if s in skill:
                valid_skill += s
                
        len_skill = len(valid_skill)
        if skill[: len_skill] == valid_skill:
            answer += 1

    return answer


TESTS = [
    # 공식 예제
    ("CBD", ["BACDE", "CBADF", "AECB", "BDA"], 2),
    # 선행 스킬이 하나도 없는 스킬트리는 가능하다
    ("CBD", ["AEF"], 1),
    ("CBD", ["CBD"], 1),
    # 순서가 뒤바뀜
    ("CBD", ["BCD"], 0),
    # 중간 스킬(B)을 건너뜀
    ("CBD", ["CD"], 0),
]


if __name__ == "__main__":
    for skill, skill_trees, expected in TESTS:
        got = solution(skill, skill_trees)
        assert got == expected, f"{(skill, skill_trees)} -> {got}, 기대값 {expected}"
    print("통과")
