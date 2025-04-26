num = int(input())
result = []
for i in range(num):
    k = int(input()) + 1
    n = int(input())
    room = [[0]*n for _ in range(k)]
    for i in range(k):
        for j in range(1,n+1):
            if(i == 0): 
                room[i][j-1] = j
            else:
                for m in range(j):
                    room[i][j-1] += room[i-1][m]
    result.append(room[k-1][n-1])
print(*result,sep="\n")