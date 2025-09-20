v,e = map(int,input().split())
edge_list = []

for i in range(e):
    a,b,c = map(int,input().split())
    edge_list.append((a,b,c))

parent = [-1] * (v+1)

def union(a,b):
    fa = find(a)
    fb = find(b)
    if fa == fb:
        return False
    if abs(parent[fa]) < abs(parent[fb]):
        parent[fa] += parent[fb]
        parent[fb] = fa
    else:
        parent[fb] += parent[fa]
        parent[fa] = fb
    return True

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def kruskal(edge_list):
    edge_list = sorted(edge_list, key=lambda x: x[2])
    mst = []
    result = 0
    for u, v, w in edge_list:
        if union(u, v):
            result += w
            mst.append((u, v, w))
    return result, mst

x,y = kruskal(edge_list)