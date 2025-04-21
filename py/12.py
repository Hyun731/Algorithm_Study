l = int(input())
room = list(input())
cnt = 0
sum = 0
mod = 1234567891
for i in room:
    sum += (ord(i)-96)*(31**cnt)
    cnt+=1
print(sum%mod)
#꼬임 해결,,