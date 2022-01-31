'''
    Walmart Question 12: Find Array Given Subset Sums

You are given an integer n representing the length of an unknown array that you are trying to recover. You are also given an array sums containing the values of all 2n subset sums of the unknown array (in no particular order).
Return the array ans of length n representing the unknown array. If multiple answers exist, return any of them.
An array sub is a subset of an array arr if sub can be obtained from arr by deleting some (possibly zero or all) elements of arr. The sum of the elements in sub is one possible subset sum of arr. The sum of an empty array is considered to be 0.

'''
import bisect
import copy
class Solution:
    def subfun(n,sums):
        if n==1:
            return [sum(sums),]
        
		# sums have been sorted by sums.sort()
        the_num=sums[-1]-sums[-2]
        the_num_cnt1=bisect.bisect_right(sums,the_num)-bisect.bisect_left(sums,the_num)
        if the_num_cnt1<=0:
            the_num*=-1
        else:
            sums_cp=copy.copy(sums)
            
        sub_sums=[]
        if the_num>=0:
            while len(sums)>0:
                pop_target=sums.pop(-1)-the_num
                sub_sums.insert(0,pop_target)
                sums.pop(bisect.bisect_left(sums,pop_target))
        else:
            while len(sums)>0:
                pop_target=sums.pop(0)-the_num
                sub_sums.append(pop_target)
                sums.pop(bisect.bisect_left(sums,pop_target))
        
        # if the_num we used is illegal
        zero_cnt=bisect.bisect_right(sub_sums,0)-bisect.bisect_left(sub_sums,0)
        if zero_cnt<=0:
            the_num*=-1
            sub_sums=[]
            sums=sums_cp
            if the_num>=0:
                while len(sums)>0:
                    pop_target=sums.pop(-1)-the_num
                    sub_sums.insert(0,pop_target)
                    sums.pop(bisect.bisect_left(sums,pop_target))
            else:
                while len(sums)>0:
                    pop_target=sums.pop(0)-the_num
                    sub_sums.append(pop_target)
                    sums.pop(bisect.bisect_left(sums,pop_target))

        return [the_num,]+Solution.subfun(n-1,sub_sums)
    
    def recoverArray(self, n: int, sums):
        sums.sort()
        return Solution.subfun(n,sums)