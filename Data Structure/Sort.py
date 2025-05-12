class Sort: #리턴값 없음
    def __init__(self):
        pass
    def merge_sort(self,a):
        n = len(a)
        if n <= 1:
            return
        mid = n//2
        g1 = a[:mid]
        g2 = a[mid:]
        self.merge_sort(g1)
        self.merge_sort(g2)
        i1 = 0
        i2 = 0
        ia = 0
        while i1 < len(g1) and i2 < len(g2):
            if g1[i1] < g2[i2]:
                a[ia] = g1[i1]
                i1 += 1
            else:
                a[ia] = g2[i2]
                i2 += 1
            ia += 1
        while i1 < len(g1):
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        while i2 < len(g2):
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    def ins_sort(self,a):
        n = len(a)
        for i in range(1,n):
            key = a[i]
            j = i - 1
            while(j >= 0 and a[j] > key):
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
    def sel_sort(self,a):
        for i in range(len(a) - 1):
            min_idx = i
            for j in range(i + 1,len(a)):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
    def bubble_sort(self,a):
        n = len(a)
        while True:
            changed = False
            for i in range(n-1):
                if a[i] > a[i+1]:
                    a[i],a[i+1] = a[i+1],a[i]
                    changed = True
            if not changed:
                return
    def quick_sort_sub(self,a,start,end):
        if end - start <= 0:
            return a

        pivot = a[end]
        i = start

        for j in range(start,end):
            if a[j] <= pivot:
                a[j],a[i] = a[i],a[j]
                i += 1

        a[i],a[end] = a[end],a[i]
        
        self.quick_sort_sub(a,start,i - 1)
        self.quick_sort_sub(a,i+1,end)
        
    def quick_sort(self,a): #퀵 정렬 쓰고 싶으면 이걸로 호출(위에거 아님 ㄴㄴ)
        self.quick_sort_sub(a, 0, len(a) - 1)
s = Sort()
a = [5,2,1,4,3,6,8,7,9,10]
s.merge_sort(a)
print(a)
a = [5,2,1,4,3,6,8,7,9,10]
s.ins_sort(a)
print(a)
a = [5,2,1,4,3,6,8,7,9,10]
s.sel_sort(a)
print(a)
a = [5,2,1,4,3,6,8,7,9,10]
s.bubble_sort(a)
print(a)