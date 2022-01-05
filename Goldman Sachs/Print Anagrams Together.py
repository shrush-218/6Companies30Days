'''
    Goldman Sachs Question 1: Print Anagrams Together 

Given an array of strings, return all groups of strings that are anagrams. 
The groups must be created in order of their appearance in the original array. 
Look at the sample case for clarification.

'''

class Solution:
    def Anagrams(self, words, n):
        
        d=dict()
        for i in words:
            s="".join(sorted(i))
            if d.get(s,0)==0:
                d[s]=[i]
            else:
                d[s].append(i)
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans
                       

if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

