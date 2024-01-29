
import sys

SIZE = 9
BOX_SIZE = 3

sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(SIZE)]
blank_coord = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0]

def check_row(x, n):
    for i in range(SIZE):
        if n == sudoku[x][i]: 
            return False
    return True

def check_column(y, n):
    for i in range(SIZE):
        if n == sudoku[i][y]:
            return False
    return True

def check_square(y, x, n):
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if n == sudoku[y//BOX_SIZE * BOX_SIZE + i][x//BOX_SIZE * BOX_SIZE + j]:
                return False
    return True


def dfs(n):
    if n == len(blank_coord):
        for i in sudoku: 
            print(*i) 
        exit() 
        
    for i in range(1,10):
        y = blank_coord[n][0]
        x = blank_coord[n][1]
        if check_column(x,i) and check_row(y,i) and check_square(y, x, i):
            sudoku[y][x] = i
            dfs(n+1)
            sudoku[y][x] = 0
            
            
dfs(0)
'''

import sys

SIZE = 9
BOX_SIZE = 3

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(SIZE)]
blank_coord = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0]

def is_valid(sudoku, y, x, n):
    # 행, 열, 3x3 칸에 중복된 숫자가 있는지 체크
    return all(
        n != sudoku[y][i] and
        n != sudoku[i][x] and
        n != sudoku[y // BOX_SIZE * BOX_SIZE + i // BOX_SIZE][x // BOX_SIZE * BOX_SIZE + i % BOX_SIZE]
        for i in range(SIZE)
    )

def solve_sudoku(sudoku, blank_coord, n):
    if n == len(blank_coord):
        for row in sudoku:
            print(*row)
        exit()

    y, x = blank_coord[n]
    for num in range(1, SIZE + 1):
        if is_valid(sudoku, y, x, num):
            sudoku[y][x] = num
            solve_sudoku(sudoku, blank_coord, n + 1)
            sudoku[y][x] = 0
            
solve_sudoku(sudoku, blank_coord, 0)
'''