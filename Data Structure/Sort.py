class Sort:
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
            min = i
            for j in range(i + 1,len(a)):
                if a[min] > a[j]:
                    min = j
            a[i], a[min] = a[min], a[i]

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