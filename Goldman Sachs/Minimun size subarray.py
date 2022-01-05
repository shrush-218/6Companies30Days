'''
	Goldman Sachs Question 14: Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return 
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. If there is no such subarray, 
return 0 instead.

'''

class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        
        n = len(nums)
        l,r = 0,0
        sm, minlen = 0, float('inf')
        while r <n:
            sm += nums[r]

            while sm >= target:
                minlen = min(minlen, r-l+1)
                sm -= nums[l]
                l +=1
            r +=1
        return minlen if minlen != float('inf') else 0