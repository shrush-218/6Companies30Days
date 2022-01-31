'''
    Walmart Question 13: Find the Kth Largest Integer in the Array

You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros. Return the string that represents the kth largest integer in nums.
Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.
 
'''
from heapq import heapify
from heapq import heappop
class Solution:
    def kthLargestNumber(self, nums, k):
        maxHeap = [-int(x) for x in nums]
        heapify(maxHeap)

        while k > 1:
            heappop(maxHeap)
            k -= 1
            
        return str(-maxHeap[0])