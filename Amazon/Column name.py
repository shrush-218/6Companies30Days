'''
	Amazon Question 12:  Colunn Name from Column number

Given a positive integer, return its corresponding column title 
as appear in an Excel sheet.
Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,
AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is 
named as “A”, column 2 as “B”, column 27 as “AA” and so on.

'''
#User function Template for python3
class Solution:
    def colName (self, n):
        string = ""
        while(n>0):
            rem = n%26
            if(rem==0):
                string+='Z'
                n = int(n/26)-1
            else:
                string+=chr((rem-1)+ord('A'))
                n = int(n/26)
        return(string[::-1])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    
# } Driver Code Ends