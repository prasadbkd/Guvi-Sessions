class dup:
    def missing(self,a):
        l=len(a)
        s=(a[l-1]*(a[l-1]+1))//2
        c=s-sum(a)
        print(c)
d=dup()
a=[1,2,3,4,5,7,8,9,10]
d.missing(a)
