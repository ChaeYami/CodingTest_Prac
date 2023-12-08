'''DFS'''

# recursive(재귀)

def dfs_recursive(graph, node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    # 그래프 딕셔너리에서 1: [2, 5, 9] 일 때 1에 인접한 2,5,9를 차례로 가져옴
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(graph, adj, visited)

    return visited

# stack

def dfs_stack(graph, start):
    visited = [] # 방문한 목록
    stack = [start] # 방문해야 하는 노드의 목록 (방문할 순서를 담아두는 용도)

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        top = stack.pop() # 제일 최근에 삽입된 노드를 꺼내 (방문)
        visited.append(top) # 방문 완료
        # print('현재 노드',top)
        # print('방문한 노드', visited)
        
        # 인접 노드를 돌아 탐색
        for adj in graph[top]: # 인접 노드들이
            # print('현재 노드의 인접 노드', adj)
            if adj not in visited: #방문한 적이 없다면
                stack.append(adj)
                # print('방문해야 할 노드',stack)

    return visited

'''dfs 예제'''

#stack

def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt

assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


# recursive

def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(m):
        for c in range(n):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt


assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

