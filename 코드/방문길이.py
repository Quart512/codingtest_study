def solution(dirs):
    answer = 0
    now = (0, 0)
    move_set = set()
    
    def see_next(direction, coordinate):
        if direction == "L":
            return (coordinate[0] - 1, coordinate[1])
        if direction == "R":
            return (coordinate[0] + 1, coordinate[1])
        if direction == "U":
            return (coordinate[0], coordinate[1] + 1)
        if direction == "D":
            return (coordinate[0], coordinate[1] - 1)
    
    for dir in dirs:
        next_step = see_next(dir, now)
        
        if -5 <= next_step[0] <= 5 and -5 <= next_step[1] <= 5:
            
            route = (now, next_step)
            reverse_route = (next_step, now)
            
            if route not in move_set and reverse_route not in move_set: 
                answer += 1

            move_set.add(route)
            now = next_step

    return answer


TESTS = [
    # 공식 예제
    ("ULURRDLLU", 7),
    ("LULLLLLLU", 7),
    # 같은 길을 되돌아오면 새 길이 아니다
    ("UD", 1),
    ("RL", 1),
    # 경계를 넘는 명령은 무시
    ("UUUUUUUUUU", 5),
]


if __name__ == "__main__":
    for dirs, expected in TESTS:
        got = solution(dirs)
        assert got == expected, f"{dirs} -> {got}, 기대값 {expected}"
    print("통과")
