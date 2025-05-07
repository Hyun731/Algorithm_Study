v,e = map(int,input().split())

adj_matrix = [[0] * (v + 1) for _ in range(v + 1)]
adj_list = [[] for _ in range(v + 1)]

for i in range(e):
    x,y = map(int,input().split())
    adj_matrix[x][y] = 1
    adj_matrix[y][x] = 1
    adj_list[x].append(y)
    adj_list[y].append(x)
    
for i in range(v + 1):
    print(*adj_matrix[i])
print(adj_list)