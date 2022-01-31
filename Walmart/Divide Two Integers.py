'''
    Walmart Question 15: Divide Two Integers
    
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

'''
class Solution:
    def divide(self, dividend, divisor):
        if abs(divisor) >abs(dividend):
            return 0
        count = 0
        label = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            label = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = self.helper(dividend, divisor, 0, 0, 0)
        if label == 0:
            res = -res
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < - 2 ** 31:
            return - 2 ** 31
        return res


    def helper(self, dividend, divisor, current_s, count, temp_count):
        # stop recursion
        if dividend < divisor:
            return count
        # stop recursion
        if dividend == divisor:
            return count + 1
        # init
        if current_s == 0:
            current_s = divisor
        # init
        if temp_count == 0:
            temp_count = 1
        #  if current divisor (names temp count) * 2 is larger than dividend, than in next loop, try future divisor = current divisor * 2
        if dividend > current_s + current_s:
            return self.helper(dividend - current_s - current_s, divisor, current_s + current_s, count + temp_count + temp_count, temp_count + temp_count)
        # if above step fail
        if dividend > current_s:
            return self.helper(dividend - current_s, divisor, current_s, count + temp_count, temp_count)
        # else divisor start from the base divisor
        if dividend > divisor:
            return self.helper(dividend - divisor, divisor, divisor, count + 1, 1)