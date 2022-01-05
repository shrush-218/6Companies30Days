
'''
	Goldman Sachs Question 6: Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x 
divides both str1 and str2. 

'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2
        if len(str2)>len(str1):
            return self.gcdOfStrings(str2, str1)
        
        elif str1.startswith(str2):
            return self.gcdOfStrings(str1[len(str2):],str2)
        else:
            return ''
        