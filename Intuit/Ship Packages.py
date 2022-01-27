'''
	Intuit Question 7: Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within 
days days. The ith package on the conveyor belt has a weight of weights[i]. Each day, 
we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on 
the conveyor belt being shipped within days days.

'''
class Solution:
    def shipWithinDays(self, weights, D) -> int:
        def cannot_split(weights, D, max_wgt):
            s = 0
            days = 1
            for w in weights:
                s += w
                if s > max_wgt:
                    s = w
                    days += 1
            return days > D
        
        low, high = max(weights), sum(weights)
        while low < high:
            mid = low + (high - low) // 2
            if cannot_split(weights, D, mid):
                low = mid + 1
            else:
                high = mid
        return low