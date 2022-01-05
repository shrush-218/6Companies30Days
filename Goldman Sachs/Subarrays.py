'''
	Goldman Sachs Question 3: Count subarrays having product less than k

Count the subarrays having product less than k.
Given an array of positive numbers, the task is to find the 
number of possible contiguous subarrays having product less 
than a given number k.

'''

#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        i=0
        j=0
        count=0
        prod=1
        for i in range(0,n):
            prod*=a[i]
            while prod>=k:
                prod/=a[j]
                j+=1
            count+=i-j+1
            
        return count
  

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends