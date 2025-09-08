n = int(input())
parent = [-1] * (n+1)

def union(a,b):
    fa = find(a)
    fb = find(b)
    if abs(parent[fa]) <= abs(parent[fb]):
        parent[fa] += parent[fb]
        parent[fb] = fa
    else:
        parent[fb] += parent[fa]
        parent[fa] = fb

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]
