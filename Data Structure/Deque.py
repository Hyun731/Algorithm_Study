class Deque:
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
    def delete_front(self): #s
        if self.isEmpty():
            return "아무것도 없습니다."
        p = self.arr[self.f]
        self.arr[self.f] = None
        self.f = (self.f + 1) % self.size
        return p
    def delete_rear(self):
        if self.isEmpty():
            return "아무것도 없습니다."
        self.r = (self.r - 1 + self.size) % self.size
        p = self.arr[self.r]
        self.arr[self.r] = None
        return p
    def add_rear(self, a): #s
        if not self.isFull():
            self.arr[self.r] = a
            self.r = (self.r + 1) % self.size
        else:
            print("자리가 없습니다.")
    def add_front(self, a):
        if not self.isFull():
            self.f = (self.f - 1 + self.size) % self.size
            self.arr[self.f] = a
        else:
            print("자리가 없습니다.")

a = Deque(4)
