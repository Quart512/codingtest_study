def solution(park, routes):
    park_matrix = [list(row) for row in park]

    H = len(park_matrix)
    W = len(park_matrix[0])

    answer = [0, 0]
    for y in range(H):
        for x in range(W):
            if park_matrix[y][x] == 'S':
                answer = [y, x]
                break

    def check(direction, n):
        nonlocal answer
        y, x = answer[0], answer[1]

        if direction == 'E':
            if x + n >= W:
                return
            for i in range(1, n + 1):
                if park_matrix[y][x + i] == 'X':
                    return
            answer = [y, x + n]

        elif direction == 'W':
            if x - n < 0:
                return
            for i in range(1, n + 1):
                if park_matrix[y][x - i] == 'X':
                    return
            answer = [y, x - n]

        elif direction == 'N':
            if y - n < 0:
                return
            for i in range(1, n + 1):
                if park_matrix[y - i][x] == 'X':
                    return
            answer = [y - n, x]

        elif direction == 'S':
            if y + n >= H:
                return
            for i in range(1, n + 1):
                if park_matrix[y + i][x] == 'X':
                    return
            answer = [y + n, x]

    for move in routes:
        direction, n = move.split(' ')
        check(direction, int(n))

    return answer


TESTS = [
    (["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"], [2, 1]),
    (["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"], [0, 1]),
    (["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"], [0, 0]),
    (["OOO", "OSO", "OOO"], ["N 1", "W 1", "S 2", "E 2"], [2, 2]),
    (["SOO", "OOO", "OOO"], ["W 1", "N 1"], [0, 0]),
]


if __name__ == "__main__":
    for park, routes, expected in TESTS:
        got = solution(park, routes)
        assert got == expected, f"{(park, routes)} -> {got}, 기대값 {expected}"
    print("통과")
