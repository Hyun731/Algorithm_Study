import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())

graph = { i : [] for i in range(1,v+1)}
min_weight = [float('inf') for _ in range(v+1)]

k = int(input())
min_weight[k] = 0
q = [(0,k)]

for _ in range(e):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

while q:
    weight, node = heapq.heappop(q)
    if weight > min_weight[node]:
            continue
    for n_weight,friends in graph[node]:
        if weight + n_weight < min_weight[friends]:
            min_weight[friends] = weight + n_weight
            heapq.heappush(q, (weight + n_weight, friends))

for i in range(1, v+1):
    if min_weight[i] == float('inf'):
        print("INF")
    else:
        print(min_weight[i])