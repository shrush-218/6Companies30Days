'''
    Goldman Sachs Question 4: Run Length Encoding

Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and returns the encoded string.

'''



#Your task is to complete this function
#Function should return complete string
def encode(arr):
    i =0 
    strr=""
    
    while i<len(arr):
        temp=arr[i]
        count=1
        while i+1<len(arr) and temp==arr[i+1]:
            i=i+1
            count+=1
        strr+=temp+str(count)
        i=i+1
    return strr

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends