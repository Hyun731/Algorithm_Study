from collections import deque

graph = {
    1: [2,3,7],
    2: [1,4,5],
    3: [1,6,7],
    4: [2,8],
    5: [2,9],
    6: [3,10],
    7: [3,1],
    8: [4],
    9: [5],
    10: [6]
}

#DFS (스택으로도 구현가능함. 현재는 재귀)
visited = { i : False for i in range(1,11)}
sequence = []

def f(x):
    visited[x] = True
    sequence.append(x)
    for node in graph[x]:
        if not visited[node]:
            f(node)

f(1)
print(sequence)

#BFS
visited = { i : False for i in range(1,11)}
sequence = []

queue = deque([1])
visited[1] = True
while queue:
    node = queue.popleft()
    sequence.append(node)
    for vertex in graph[node]:
        if not visited[vertex]:
            visited[vertex] = True
            queue.append(vertex)
            
print(sequence)
