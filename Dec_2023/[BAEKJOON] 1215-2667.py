import sys

input = sys.stdin.readline

map_size = int(input())

complex = []
for i in range(map_size):
    row = list(map(int, input().rstrip()))
    complex.append(row)
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0

for row in range(map_size):
    for col in range(map_size):
        if complex[row][col] == '0':
            continue
        
        cnt += 1
        stack = [(row,col)]
        
        while stack:
            x,y = stack.pop()