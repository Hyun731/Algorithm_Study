#이스터에그
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
edges = []
min_weight = [float('inf') for _ in range(v+1)]

k = int(input())
min_weight[k] = 0

for _ in range(e):
    a,b,w = map(int,input().split())
    edges.append((a,b,w))
    edges.append((b,a,w))

for _ in range(v-1):
    for c,d,w in edges:
        if min_weight[c] + w < min_weight[d]:
            min_weight[d] = min_weight[c] + w

isChange = False
for c,d,w in edges:
    if min_weight[c] + w < min_weight[d]:
        isChange = True
        break
    
if isChange:
    print("yes")
else:
    print("no")