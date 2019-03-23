class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
def inorder(root): 
    
    if root: 
        
        inorder(root.left) 
        
        print(root.val) 
        inorder(root.right) 
        
    #print(count,"is height")
def maxDepth(node): 
    if node is None: 
        return 0 ;  
  
    else : 
  
        
        l = maxDepth(node.left) 
        r = maxDepth(node.right) 
  
        if (l > r): 
            print("l",l,"node=",node.val)
            return l+1
        else: 
            print("r",r,"node=",node.val)
            return r+1

    
    
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
insert(r,Node(90))
inorder(r) 
print(maxDepth(r))
