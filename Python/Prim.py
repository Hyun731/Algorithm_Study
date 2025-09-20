import heapq
import sys
input = sys.stdin.readline

p, o = map(int, input().split())
edge_list = []

for _ in range(o):
    a, b, c = map(int, input().split())
    edge_list.append((a-1, b-1, c))  # 0-index로 변환

n = p
graph = [[] for _ in range(n)]
for u, v, w in edge_list:
    graph[u].append((w, v))
    graph[v].append((w, u))

def Prim(start=0):
    visited = [False] * n
    queue = [(0, start, -1)]
    result = 0
    mst = []

    while queue:
        w, v, parent = heapq.heappop(queue)
        if visited[v]:
            continue
        visited[v] = True
        result += w
        if parent != -1:
            mst.append((parent, v, w))
        for nw, u in graph[v]:
            if not visited[u]:
                heapq.heappush(queue, (nw, u, v))

    return result, mst

total, edges = Prim()
edges = sorted(edges, key=lambda x:x[2])
print(total - edges[-1][2])