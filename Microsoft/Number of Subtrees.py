'''
	Microsoft Question 9: Count Number of SubTrees having given Sum 

Given a binary tree and an integer X. Your task is to complete the function 
countSubtreesWithSumX() that returns the count of the number of subtress 
having total nodes data sum equal to the value X.     

'''
def helper(root,x):
    if not root:
        return [0,0]
    l,r = helper(root.left,x), helper(root.right,x)
    if (root.data+l[0]+r[0])==x:
        return [root.data+l[0]+r[0],1+l[1]+r[1]]
    else:
        return [root.data+l[0]+r[0],l[1]+r[1]]
def countSubtreesWithSumX(root, x):
    return helper(root,x)[1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(100000);
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        x = int(input())
        print(countSubtreesWithSumX(root,x))
        
        


# } Driver Code Ends