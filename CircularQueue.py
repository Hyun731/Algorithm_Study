class CircularQueue:
    arr : list
    f : int
    r : int
    size : int
    def __init__(self,size):
        self.arr = [0]*size
        self.f = 0
        self.r = 0
        self.size = size
    def isFull(self):
        if (self.r + 1) % self.size == self.f: return True
        return False
    def isEmpty(self):
        return self.f == self.r
    def dequeue(self):
        if self.isEmpty():
            return "아무것도 없습니다."
        self.f = (self.f + 1) % self.size
        p = self.arr[self.f]
        self.arr[self.f] = None
        return p
    def enqueue(self, a):
        if not self.isFull():
            self.r = (self.r + 1) % self.size
            self.arr[self.r] = a
        else:
            print("자리가 없습니다.")


