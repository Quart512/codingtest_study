def solution(n):
    full_list = [i+1 for i in range(int(n*(n+1)/2))]
    full_dict = {i: 0 for i in full_list}
    full_dict_layer = {i: 0 for i in full_list}

    now_layer=1
    for block in full_list:
        if int(now_layer*(now_layer+1)/2)<block:
            now_layer+=1
        full_dict_layer[block]=now_layer

    def left_down(now):
        now_layer = full_dict_layer[now]
        return now+now_layer
    def right(now):
        return now+1
    def left_up(now):
        now_layer = full_dict_layer[now]
        return now - now_layer

    def turn(direction):
        if direction == left_down:
            return right
        if direction == right:
            return left_up
        if direction == left_up:
            return left_down

    direction_list=[]
    for i in range(n):
        direction_list.insert(i,n-i)
    direction_list[0]-=1
    direction_list.insert(-1,1)

    target=1
    num=1
    direction_now=left_down
    for moves in direction_list:
        for move in range(moves):
            full_dict[target]=num
            num+=1
            target = direction_now(target)
        direction_now = turn(direction_now)

    return  [v for v in full_dict.values()]


TESTS = [
    (1, [1]),
    (4, [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]),
    (5, [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]),
    (6, [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]),
]


if __name__ == "__main__":
    for n, expected in TESTS:
        got = solution(n)
        assert got == expected, f"n={n} -> {got}, 기대값 {expected}"
    # 문제 최대 입력(n=1000)에서 시간 초과가 안 나는지
    import time
    t = time.time()
    solution(1000)
    print(f"통과 (n=1000: {time.time() - t:.3f}s)")
