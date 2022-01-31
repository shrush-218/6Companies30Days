'''
    Walmart Question 8: Maximum Height Tree

Given N dots that form a triangle such that ith line contains i number of dots.

    .
   . .
  . . .
 . . . .
Find the minimum hieght H of the triangle that can be formed using these N dots.

'''
class Solution:
    def height(self, N):
        i = 1
        res = 1
        while res <= N:
            res += i + 1
            i += 1
        return i - 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.height(N))
