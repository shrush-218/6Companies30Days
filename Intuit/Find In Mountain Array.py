'''
	Intuit Question 6: Find in Mountain Array

You may recall that an array arr is a mountain array if and only if:
arr.length >= 3 There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that 
mountainArr.get(index) == target. If such an index does not exist, return -1.
'''
class Solution:
    def findInMountainArray(self, target, mountain_arr) -> int:
            leng = mountain_arr.length()
            left, right = 0, leng-1
            # find peak
            while left < right: # there is definitely a peak, so we use '<' instead of '<='
                mid = (left+right) // 2
                if mountain_arr.get(mid) >= mountain_arr.get(mid+1):
                    right = mid
                else:
                    # 'left' and 'right' could be consecutive
                    # 'mid' intends to be 'left', so we need 'left' to plus one to avoid endless loop
                    left = mid + 1 
            peak = left
            if target == mountain_arr.get(peak):
                return peak

            # search behind the peak
            l, r = 0, peak-1
            while l <= r: # there may not be a target behind the peak, so using '<='
                print(l, r, end =' ')
                mid = (l + r) // 2
                print('1:', mid)
                cur = mountain_arr.get(mid)
                if cur == target:
                    return mid
                elif cur > target:
                    r = mid - 1
                else:
                    l = mid + 1

            # search after the peak
            l, r = peak+1, leng-1
            while l <= r: # there may not be a target after the peak, so using '<='
                print('2:', mid)
                mid = (l + r) // 2
                cur = mountain_arr.get(mid)
                if cur == target:
                    return mid
                elif cur > target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1