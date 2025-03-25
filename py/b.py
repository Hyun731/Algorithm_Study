n = int(input())
a = n
li = []
x, y = 0, 0
low = 1
val = 0
for i in range(n):
    li.append([])
    for j in range(n):
        li[i].append(0)
for i in range(n):
    x = i
    val += 1
    li[y][x] = val
n -= 1
val += 1

while n!=0:
    if low==True:
        for i in range(n):
            y += 1
            li[y][x] = val
            val += 1
        for i in range(n):
            x -= 1
            li[y][x] = val
            val += 1
        n -= 1
        low = 0
    else:
        for i in range(n):
            y -= 1
            li[y][x] = val
            val += 1
        for i in range(n):
            x += 1
            li[y][x] = val
            val += 1
        n -= 1
        low = 1

for i in range(a):
    print(*li[i])