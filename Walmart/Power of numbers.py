'''
    Walmart Question 6: Power of numbers

Given a number and its reverse. Find that number raised to the power of its own reverse.
Note: As answers can be very large, print the result modulo 109 + 7.

'''
class Solution:
    def power(self,N,R):
        M = 1000000007
        N %= M
        if R == 0:
            return 1
        if R == 1:
            return N
        tmp = self.power(N, R // 2)
        res = (tmp * tmp) % M
        if R % 2 != 0:
            res = (res * N) % M
        return res

import math
def main():   
    T=int(input())
    while(T>0):   
        N=input()
        R=N[::-1]
        ob=Solution()
        ans=ob.power(int(N),int(R))
        print(ans)   
        T-=1

if __name__=="__main__":
    main()
