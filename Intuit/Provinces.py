'''
	Intuit Question 10: Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is 
connected directly with city c, then city a is connected indirectly with city c. A province is a group of directly or indirectly 
connected cities and no other cities outside of the group. You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

'''
from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected) -> int:
        N = len(isConnected)
        visited = [False] * N

        conn = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if i != j:
                    if isConnected[i][j] == 1:
                        conn[i].append(j)

        def dfs(i):
            for j in conn[i]:
                if visited[j] == False:
                    visited[j] = True
                    dfs(j)

        nprov = 0
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                nprov += 1
                dfs(i)

        return nprov
        