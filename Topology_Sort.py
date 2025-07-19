from collections import deque

graph = {
    1 : [2,4],
    2 : [3],
    3 : [],
    4 : [3,5],
    5 : []
}

o = list()

q = deque()
in_degree = [0,0,1,2,1,1]

for i in range(1,len(in_degree)):
    if in_degree[i] == 0:
        q.append(i)
while q:
    node = q.popleft()
    o.append(node)
    for i in graph[node]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
print(o)