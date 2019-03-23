class a:
    def __init__(self):
        self.top=0
        self.s=[0,0,0]
    
    
    def push(self,b):
        self.app
        self.s[self.top]=b
        self.top+=1
        print("pushed b")
    def pop(self):
        
        if self.top==0:
            print("empty")
        else:
            print(self.s[self.top-1],"item popped")
            self.s[self.top-1]=0
            
            
            self.top-=1
        print(self.s)
        
        
o=a()
o.push(10)
o.push(20)
o.push(20)
o.pop()
o.pop()
o.pop()
o.pop()
