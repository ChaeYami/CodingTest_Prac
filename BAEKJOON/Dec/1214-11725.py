# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

""" DFS """

'''
첫번째 예시라면 
grahp = {
    1: {4, 6}, 
    2: {4}, 
    3: {5, 6}, 
    4: {1, 2, 7}, 
    5: {3}, 
    6: {1, 3}, 
    7: {4}
    }
'''
'''
처음 딕셔너리로 구현했으나 set 사용에 시간이 더 걸려서 인접 리스트로 변경

graph = {} # 그래프 딕셔너리 생성

for i in range(1, N+1):
    graph[i] = set()

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)
    
'''
# 그래프 생성
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부, 각 인덱스를 노드로 사용해 방문했으면 0을 지우고, 부모 노드를 저장한다.
visited = [0]*(N+1) 

'''dfs - 재귀함수로 구현'''
def dfs(node):
    for i in graph[node]: # 해당 노드에 인접한 노드 중에서
        if visited[i] == 0: # 방문한 적이 없다면
            visited[i] = node # 해당 노드를 부모 노드로 저장
            dfs(i)

dfs(1)
# 첫번째 예시라면 visited = [0, 4, 4, 6, 1, 3, 1, 4]

for x in range(2, N+1):
    print(visited[x]) # 각 인덱스(노드)에 저장된 부모 노드 가져오기

'''dfs - 스택으로 구현'''
def dfs(graph,node):

    stack = [node]
    while stack:
        top = stack.pop()
        for adj in graph[top]:
            if visited[adj] == 0: # 방문한 적이 없다면
                visited[adj] = top # 해당 노드를 부모 노드로 저장
                stack.append(adj)
    
    return visited

dfs(graph,1)
# 첫번째 예시라면 visited = [0, 4, 4, 6, 1, 3, 1, 4]

for x in range(2, N+1):
    print(visited[x]) # 각 인덱스(노드)에 저장된 부모 노드 가져오기



""" BFS """


graph = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)

def bfs(start):
    deq = deque([start]) # 방문할 노드
    
    while deq:
        node = deq.popleft()
        
        for adj in graph[node]:
            if visited[adj] == 0:
                visited[adj] = node
                deq.append(adj)

bfs(1)
answer = visited[2:]
for x in answer:
    print(x)


