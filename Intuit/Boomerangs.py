'''
	Intuit Question 8: Number of Boomerangs

You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. 
A boomerang is a tuple of points (i, j, k) such that the distance between i and j 
equals the distance between i and k (the order of the tuple matters).
Return the number of boomerangs.
'''
class Solution:
	def numberOfBoomerangs(self, p) -> int:
		L, t = len(p), 0
		D = [[0]*L for i in range(L)]
		for i in range(L):
			E = {}
			for j in range(L):
				if j > i: D[i][j] = D[j][i] = (p[j][0]-p[i][0])**2 + (p[j][1]-p[i][1])**2
				E[D[i][j]] = E[D[i][j]] + 1 if D[i][j] in E else 1
			t += sum(r*(r-1) for r in E.values())
		return t
		