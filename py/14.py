def f(n):
    if room[n] != 10**5:
        return room[n]
    a,b,c = 10**5,10**5,10**5
    if(n % 2 == 0):
        a = f(n//2)+1
    if(n % 3 == 0):
        b = f(n//3) + 1
    c = f(n-1) + 1
    room[n] = min(a,b,c)
    return room[n]

n = int(input())
room = [10**5] * 10**6 + 1
room[1] = 0
room[2] = 1
room[3] = 1
print(f(n))
