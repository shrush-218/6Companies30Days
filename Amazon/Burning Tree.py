'''
	Amazon Question 14:  Burning Tree

Given a binary tree and a node called target. Find the minimum time required 
to burn the complete binary tree if the target is set on fire. It is known 
that in 1 second all nodes connected to a given node get burned. That is its 
left child, right child, and parent.

'''
#User function Template for python3

class Solution:
    def minTime(self, root,target):
        # code here
        burned = set()
        parent = {}
        child={}
        q = deque()
        q.append(root)
        while(q):
            size = len(q)
            while(size):
                ele = q.popleft()
                if ele.left:
                    if ele.left.data in parent:
                        parent[ele.left.data].append(ele.data)
                    else:
                        parent[ele.left.data] = [ele.data]
                    if  ele.data in child:
                        child[ele.data].append(ele.left.data)
                    else:
                        child[ele.data] = [ele.left.data]
                    q.append(ele.left)
                if ele.right:
                    if ele.right.data in parent:
                        parent[ele.right.data].append(ele.data)
                    else:
                        parent[ele.right.data] = [ele.data]
                    if  ele.data in child:
                        child[ele.data].append(ele.right.data)
                    else:
                        child[ele.data] = [ele.right.data]
                    q.append(ele.right)
                size -= 1        
        time = 0
        burned.add(target)
        q2 = deque()
        q2.append(target)
        while(q2):
            time+=1
            size = len(q2)
            while(size):
                node = q2.popleft()
                burned.add(node)
                if node in parent:
                    currpar = parent[node]
                    for par in currpar:
                        if par not in burned:
                            q2.append(par)
                if node in child:
                    currchild = child[node]
                    for ch in currchild:
                        if ch not in burned:
                            q2.append(ch)
                size-=1
        return time-1



#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends