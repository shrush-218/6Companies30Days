'''
	Microsoft Question 5: Stock Span Problem

The stock span problem is a financial problem where we have a series of n daily price 
quotes for a stock and we need to calculate the span of stocks price for all n days. 
The span Si of the stocks price on a given day i is defined as the maximum number of 
consecutive days just before the given day, for which the price of the stock on the 
current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, 
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

'''

class Solution:
    def calculateSpan(self,a,n):
        res = []
        s = []
        for i in range(n):
            if(len(s) == 0):
                res.append(-1)
            elif(len(s) > 0 and s[-1][0] > a[i]):
                res.append(s[-1][1])
            elif(len(s) > 0 and s[-1][0] <= a[i]):
                while(len(s) > 0 and s[-1][0] <= a[i]):
                    s.pop(-1)
                if(len(s) == 0):
                    res.append(-1)
                else:
                    res.append(s[-1][1])
            s.append([a[i],i])
        for i in range(n):
            res[i] = i - res[i]
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        print(*ans) # print space seperated elements of span array
# } Driver Code Ends