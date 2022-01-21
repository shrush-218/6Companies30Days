'''
	Adobe Question 8: Implement Atoi 

Your task  is to implement the function atoi. The function takes a string(str) as 
argument and converts it to an integer and returns it.
Note: You are not allowed to use inbuilt function.

'''
class Solution:
    def atoi(self,string):
        if (string[0] == "-" and string[1:].isnumeric()):
           return int(string)
        else:
            if (string.isnumeric()):
                return int(string)
            else:
                return -1

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip()
        ob=Solution()
        print(ob.atoi(string))
