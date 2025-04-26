def check(a,num,m):
    for i in range(num+1,m):
        if(a[i] == '('):
            check(a,num,m)
        elif(a[i] == ')'):
            a[num] = 0
            a[num+1] = 0
            print(a)

c = 1
m = int(input())
for i in range(m):
    a = list(input())
    for j in a:
        if(j == '('):
            check(a,a.index(j),m)
            print(a)
            for k in a:
                if(k != 0):
                    c = 0
                    break
            if(c):
                print("yes")
                break
        else:
            print("no")
    c = 0
    