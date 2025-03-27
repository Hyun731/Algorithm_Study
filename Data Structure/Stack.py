class Stack:
    arr : list
    t : int
    def __init__(self,size):
        self.arr = [0]*size
        self.t = -1
        
    def isFull(self):
        if self.t == (len(self.arr) - 1): return True
        return False
    def isEmpty(self):
        return self.t == -1
    def pop(self):
        if self.isEmpty():
            return "아무것도 없습니다."
        else:
            p = self.arr[self.t]
            self.t -= 1
            return p
    def push(self, a):
        if self.isFull() == False:
            self.t += 1
            self.arr[self.t] = a
        else:
            print("자리가 없습니다.")
