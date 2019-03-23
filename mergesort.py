class merge:
    def mergesort(self,ar):
        
      #  print("test")
       # print(ar)
        if len(ar)>1:
            mid=len(ar)//2
            l=ar[mid:]
            r=ar[:mid]
            m.mergesort(l)
            m.mergesort(r)
        
            i=j=k=0
            while i<len(l) and j<len(r):
                if l[i]<r[j]:
                    ar[k]=l[i]
                    i+=1
                else:
                    ar[k]=r[j]
                    j+=1
                k+=1
            while i<len(l):
                ar[k]=l[i]
                i+=1
                k+=1
            while j<len(r):
                ar[k]=r[j]
                j+=1
                k+=1
        return ar
    def print1(self):
        print(t)
m=merge()
ar1=[2,5,4,8,22,9]
#ss=ar1[:3]
print(ar1)
print(m.mergesort(ar1))
t=m.mergesort(ar1[:3])
m.print1()
#print(t)
#print(ss)
