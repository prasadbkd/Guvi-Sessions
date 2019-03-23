class node:
    def __init__(self,n):
        self.n=n
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def print1(self):
        temp=self.head
        while temp:
            print(temp.n)
            temp=temp.next
    
    def append1(self,y):
        
        tt=self.head
        while tt.next is not None:
            tt=tt.next
        ttt=node(y)
        tt.next=ttt
            
    def insert1(self,prev,new):
        newnode=node(new)
        newnode.next=prev.next
        prev.next=newnode
    def delete1(self,p):
        i=0
        j=0
        prev=self.head
        temp=self.head
        while i<p-1:
            prev=prev.next
            i+=1
        while j<p:
            temp=temp.next
            j+=1
        prev.next=temp.next
        temp=None
        
        
    def rdelete(self,r):
        count=0
        ttt=self.head
        pr=self.head
        te=self.head
        while ttt is not None:
            count+=1
            ttt=ttt.next
        ii=0
        jj=0
        while ii<count-r-1:
            pr=pr.next
            ii+=1
        while jj<count-r:
            te=te.next
            jj+=1
        pr.next=te.next
        te=None
    def checkcl(self):
        co=0
        tee=self.head
        while tee is not None:
            co+=1
            tee=tee.next
        if tee==None:
            print("its not circular linked list")
        else:
            print("its circular")
        
        
        
ll=linked()
ll.head=node(1)
sec=node(2)
ll.head.next=sec
ll.print1()
ll.insert1(ll.head,3)
ll.print1()
print()
ll.delete1(1)
ll.print1()
print()
ll.append1(3)
ll.print1()
ll.rdelete(1)
print()
ll.print1()
