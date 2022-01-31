'''
    Walmart Question 5: Transform to sub tree

Given a Binary Tree of size N , where each node can have positive or negative values. Convert this to a tree where each node contains the 
sum of the left and right sub trees of the original tree. The values of leaf nodes are changed to 0.

'''
class Solution:
    def toSumTree(self, root) :
        if root is None:
            return 0
        l=self.toSumTree(root.left)
        r=self.toSumTree(root.right)
        old_value=root.data
        root.data=l+r
        return l+r+old_value

import sys
sys.setrecursionlimit(10**6)
from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    if(len(s)==0 or s[0]=="N"):           
        return None
    ip=list(map(str,s.split()))
    
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    q.append(root)                            
    size=size+1 
    i=1                                       
    while(size>0 and i<len(ip)):
        currNode=q[0]
        q.popleft()
        size=size-1
        currVal=ip[i]
        if(currVal!="N"):
            currNode.left=Node(int(currVal))
            q.append(currNode.left)
            size=size+1
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        if(currVal!="N"):
            currNode.right=Node(int(currVal))
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def printInorder(Node) : 
    if (Node == None) : 
        return
    printInorder(Node.left)  
    print(Node.data, end = " ")  
    printInorder(Node.right)  
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        ob.toSumTree(root)
        printInorder(root)
        print()
