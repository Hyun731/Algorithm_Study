import sys
def push(room,n):
    room.append(n)

def pop(room):
    if empty(room):
        return -1
    else:
        return room.pop(0)
    
def size(room):
    return len(room)

def empty(room):
    if room: return 0
    else: return 1
    
def front(room):
    if empty(room):
        return -1
    else:
        return room[0]
    
def back(room):
    if empty(room):
        return -1
    else:
        return room[len(room)-1]
n = int(sys.stdin.readline())
room = []
for _ in range(n):
        a = sys.stdin.readline().split()
        if a[0] == 'push':
           push(room,int(a[1]))
        elif a[0] == 'pop':
            print(pop(room))
        elif a[0] == 'size':
            print(size(room))
        elif a[0] == 'empty':
            print(empty(room))
        elif a[0] == 'front':
            print(front(room))
        elif a[0] == 'back':
            print(back(room))

    