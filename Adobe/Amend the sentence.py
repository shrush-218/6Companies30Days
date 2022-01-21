'''
	Adobe Question 11: Amend The Sentence 

Given a string which is basically a sentence without spaces between words. However 
the first letter of every word is in uppercase. You need to print this sentence 
after following amendments:
(i) Put a single space between these words
(ii) Convert the uppercase letters to lowercase.

'''
class Solution:

    def amendSentence(self, s):
        output_s=s[0].lower()
        for i in s[1:]:
            if i.islower():
                output_s+=i
            else:
                output_s+=' '
                output_s+=i.lower()
        return output_s

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solObj = Solution()
        print(solObj.amendSentence(s))

