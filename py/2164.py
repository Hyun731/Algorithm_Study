class Queue:
    arr : list
    f : int
    r : int
    def __init__(self,size):
        self.arr = [0]*size
        self.f = -1
        self.r = -1
    def isFull(self):
        if self.r == (len(self.arr) - 1): return True
        return False
    def isEmpty(self):
        return self.f == self.r
    def dequeue(self):
        if self.isEmpty():
            return "아무것도 없습니다."
        else:
            self.f += 1
            p = self.arr[self.f]
            return p
    def enqueue(self, a):
        if self.isFull() == False:
            self.r += 1
            self.arr[self.r] = a
        else:
            print("자리가 없습니다.")

n = int(input())
a = Queue(1000000)
for i in range(1,n+1):
    a.enqueue(i)
while(a.r - a.f != 1):
    a.dequeue()
    if(a.r - a.f == 1):
        break
    a.enqueue(a.dequeue())
print(a.arr[a.r])