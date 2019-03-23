l=[1,1,2,2,3,4,4,5,7,9,8,9,10]
c=[]
for i in l:
    
    y=l.count(i)
    if y!=1:
        c.append(i)
        l.remove(i)
        
print(c,"are duplicates")    
