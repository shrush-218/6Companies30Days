'''
	Intuit Question 5: Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

'''
class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:
        def cannot_split(max_sum, m):
            cuts, curr_sum  = 0, 0
            for x in nums:
                curr_sum += x
                if curr_sum > max_sum:
                    cuts += 1
                    curr_sum = x
            subs = cuts + 1
            return (subs > m)
        
        low, high = max(nums), sum(nums)
        while low < high:
            guess = low + (high - low) // 2
            if cannot_split(guess, m):
                low = guess + 1
            else:
                high = guess
        return low
        