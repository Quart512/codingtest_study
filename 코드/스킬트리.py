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
