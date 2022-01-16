from collections import defaultdict
class Solution:
    def cycle(self,visited,arr,i,rec):
        visited[i]=True
        rec[i]=True
        for j in arr[i]:
            if visited[j]==False:
                if self.cycle(visited,arr,j,rec)==True:
                    return True
            elif rec[j]==True:
                return True
        rec[i]=False
        return False
    
    def isPossible(self,N,prerequisites):
    #code here
        visited=[False]*N
        rec=[False]*N
        arr=defaultdict(list)
        for i in range(0,len(prerequisites)):
            arr[prerequisites[i][1]].append(prerequisites[i][0])
        for i in range(0,N):
            if self.cycle(visited,arr,i,rec)==True:
                return 0
        return 1
    

'''
	Microsoft Question 2: Prerequisite Tasks

There are a total of N tasks, labeled from 0 to N-1. Some tasks may 
have prerequisites, for example to do task 0 you have to first complete 
task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks N and a list of prerequisite pairs P, 
find if it is possible to finish all tasks

''' 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends