'''
	Microsoft Question 4: Spirally traversing a matrix

Given a matrix of size r*c. Traverse the matrix in spiral form.

'''
class Solution:

    def spirallyTraverse(self,matrix, r, c): 
        rowbegin=0
        rowend=len(matrix)
        columnbegin=0
        columnend=len(matrix[0])
        res=[]
        while rowbegin<rowend and columnend>columnbegin:
            for i in range(columnbegin,columnend):
                res.append(matrix[rowbegin][i])
            for j in range(rowbegin+1,rowend-1):
                res.append(matrix[j][columnend-1])
            if rowend!=rowbegin+1:
                for i in range(columnend-1,columnbegin-1,-1):
                    res.append(matrix[rowend-1][i])
            if columnbegin!=columnend-1:
                for j in range(rowend-2,rowbegin,-1):
                    res.append(matrix[j][columnbegin])
            rowbegin+=1
            rowend-=1
            columnbegin+=1
            columnend-=1
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends