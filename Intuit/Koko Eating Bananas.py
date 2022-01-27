'''
	Intuit Question 15: Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and 
will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile 
of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and 
will not eat any more bananas during this hour. Koko likes to eat slowly but still wants to finish eating all the 
bananas before the guards return. 
Return the minimum integer k such that she can eat all the bananas within h hours.
    
'''
import math
class Solution:
    def minEatingSpeed(self, piles, H):
        beg, end = 0, max(piles)
        while beg+1 < end:
            mid = (beg+end)//2
            if sum(math.ceil(i/mid) for i in piles) > H:
                beg = mid
            else:
                end = mid                
        return end
        