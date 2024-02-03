
import sys

SIZE = 9

sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(SIZE)] # 스도쿠 문제
blank_coord = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0] # 빈칸의 좌표를 나타낸 리스트

def check(y, x, check_num):
    BOX_SIZE = 3
    
    for i in range(SIZE): # 가로, 세로 체크
        if sudoku[y][i] == check_num or sudoku[i][x] == check_num:
            return False
    
    for i in range(BOX_SIZE): # 3x3영역 체크
        for j in range(BOX_SIZE):
            if sudoku[y // BOX_SIZE * BOX_SIZE + i][x // BOX_SIZE * BOX_SIZE + j] == check_num:
                return False
    return True

def dfs(n):
    if n == len(blank_coord):
        for i in sudoku: 
            print(*i) 
        exit() 
    
    for check_num in range(1,10):
        y, x = blank_coord[n]
        # y = blank_coord[n][0]
        # x = blank_coord[n][1]
        if check(y, x, check_num):
            sudoku[y][x] = check_num
            dfs(n+1)
            sudoku[y][x] = 0
            
dfs(0)


import sys

SIZE = 9

sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(SIZE)]
    # 스도쿠 퍼즐의 모든 셀의 합 초기화
total_sum = sum(map(sum, sudoku))

def check(y, x, check_num):
    BOX_SIZE = 3
    
    for i in range(SIZE): # 가로, 세로 체크
        if sudoku[y][i] == check_num or sudoku[i][x] == check_num:
            return False
    
    for i in range(BOX_SIZE): # 3x3영역 체크
        for j in range(BOX_SIZE):
            if sudoku[y // BOX_SIZE * BOX_SIZE + i][x // BOX_SIZE * BOX_SIZE + j] == check_num:
                return False
    return True

def dfs(n, current_sum):
    global total_sum

    if total_sum == 405:
        # 총 합이 405이면 종료
        for x in sudoku:
            print(*x)
        return True

    # 일차원 리스트 인덱스를 이차원 좌표로 변환
    y = n // SIZE # y좌표
    x = n % SIZE # x좌표

    # 해당 칸의 숫자가 0이라면 탐색 
    if sudoku[y][x] == 0:
        for check_num in range(1, 10):
            
            if check(y, x, check_num): # 조건에 맞다면 숫자를 채우고 합함
                sudoku[y][x] = check_num
                total_sum += check_num
                
                if dfs(n + 1, current_sum + check_num):  # 재귀 : 다음 위치로 이동
                    return True
                '''
                실패하면 - dfs(n+1)에서 1~9까지 다 넣어도 통과하지 못한다
                dfs(n)에 넣은 수가 잘못된 것이므로 다른 숫자로 시도해보기 위해 원래 상태로 되돌림
                '''
                sudoku[y][x] = 0
                total_sum -= check_num
                
    else: # 0이 아니라면 다음 위치로 이동
        return dfs(n + 1, current_sum)

dfs(0, 0)
