'''
	Intuit Question 12: Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take 
course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any 
of them. If it is impossible to finish all courses, return an empty array.
'''

from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        degree = defaultdict(int)   
        graph = defaultdict(set)
        q = deque()
        
        
        for i in range(numCourses):
            degree[i] = 0
        
        for pair in prerequisites:
            degree[pair[0]] += 1
            graph[pair[1]].add(pair[0])
        
        for key, val in degree.items():
            if val == 0:
                q.append(key)
                
        stack = []
        
        while q:
            curr = q.popleft()
            stack.append(curr)
            for child in graph[curr]:
                degree[child] -= 1
                if degree[child] == 0:
                    q.append(child)
        
        if len(stack) != numCourses:
            return []
        else:
            return stack