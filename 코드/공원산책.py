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
            # 1) 범위 체크
            if x + n >= W:
                return
            # 2) 이동 경로 상 장애물 체크 (1부터 n까지 한 칸씩 검사)
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
