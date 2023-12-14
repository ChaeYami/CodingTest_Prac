from collections import deque
graph = { 
		 1: [2, 5, 9], 
		 2: [1, 3], 
		 3: [2, 4], 
		 4: [3], 
		 5: [1, 6, 8], 
		 6: [5, 7], 
		 7: [6], 
		 8: [5], 
		 9: [1, 10], 
		 10: [9] 
		 }

def bfs_queue(graph, start):
    visited = [] # 방문한 노드
    q = deque([start]) # 방문해야 할 노드

    while q:
        node = q.popleft()
        visited.append(node)
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                

    return visited

print(bfs_queue(graph, 1)) # [1, 2, 5, 9, 3, 6, 8, 10, 4, 7]