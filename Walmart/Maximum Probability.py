'''
    Walmart Question 1: Path With Maximum Probability 

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge 
connecting the nodes a and b with a probability of success of traversing that edge succProb[i]. Given two nodes start and end, find the path 
with the maximum probability of success to go from start to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

'''
import collections
import heapq
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        
        graph = collections.defaultdict(list)
        prob = collections.defaultdict(dict)
        for i,(p,[a,b]) in enumerate(zip(succProb,edges)):
            graph[a].append(b)
            graph[b].append(a)
            prob[a][b] = prob[b][a] = p
        dis = {start:1}
        for i in range(n):
            dis[i] = 0
        visited = set([])
        pq = [(-1,start)]
        while pq:
            _p, node = heapq.heappop(pq)
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    if dis[child] < -1 * _p * prob[node][child]:
                        heapq.heappush(pq,(_p * prob[node][child],child))
                        dis[child] = -1 * _p * prob[node][child]

        return dis[end]