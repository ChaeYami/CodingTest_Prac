def solution(edges):
    answer = []
    
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    n = len(graph)

    donut_cnt = 0
    bar_cnt = 0
    eight_cnt = 0

    def dfs(node, visited, is_donut, is_bar, is_eight):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, is_donut, is_bar, is_eight)

        if len(graph[node]) == 2:
            is_bar[0] = True
        elif len(graph[node]) == 3:
            is_eight[0] = True

    visited = {node: False for node in graph}

    for node in graph:
        if not visited[node]:
            is_donut = [False]
            is_bar = [False]
            is_eight = [False]
            dfs(node, visited, is_donut, is_bar, is_eight)

            if is_eight[0]:
                eight_cnt += 1
            elif is_bar[0]:
                bar_cnt += 1
            elif is_donut[0]:
                donut_cnt += 1
                
    answer = [n + 1, donut_cnt, bar_cnt, eight_cnt]
    return answer