class Stack:
    arr : list
    t : int
    size : int
    def __init__(self,size):
        self.size = size
        self.arr = [0]*size
        self.t = -1
    def isFull(self):
        if self.t == self.size - 1: return True
        return False
    def isEmpty(self):
        return self.t == -1
    def pop(self):
        if self.isEmpty():
            return "아무것도 없습니다."
        p = self.arr[self.t]
        self.t -= 1
        return p
    def push(self, a):
        if not self.isFull():
            self.t += 1
            self.arr[self.t] = a
        else:
            print("자리가 없습니다.")
