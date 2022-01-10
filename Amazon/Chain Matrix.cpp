'''
	Amazon Question 4:  Brackets in Matrix Chain Multiplication

Given an array p[] of length n used to denote the dimensions of a series of matrices such that 
dimension of ith matrix is p[i] * p[i+1]. There are a total of n-1 matrices. 
Find the most efficient way to multiply these matrices together. The problem is not actually 
to perform the multiplications, but merely to decide in which order to perform the multiplications 
such that you need to perform minimum number of multiplications. There are many options to multiply a 
chain of matrices because matrix multiplication is associative i.e. no matter how one parenthesize the 
product, the result will be the same.

'''

// { Driver Code Starts
// Initial Template for C++


using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution {
    
    map<string, pair<int, string>> dp;
    
  public:
    string matrixChainOrder(int A[], int n) {
        return matrixChainOrderUtil(A, 0, n - 1).second;
    }
        pair<int, string> matrixChainOrderUtil(int p[], int l, int r) {
    	if(l + 1 == r) return {0, "" + string(1, l + 'A')};
        string key = to_string(l) + ";" + to_string(r);
        if(dp.count(key)) return dp[key];
                int currMin = INT_MAX;
        string minString;
        for(int k = l + 1; k < r; k++) {
            auto p1 = matrixChainOrderUtil(p, l, k), p2 = matrixChainOrderUtil(p, k, r);
            if(p1.first + p2.first + p[l] * p[k] * p[r] < currMin) {
                currMin = p1.first + p2.first + p[l] * p[k] * p[r];
                
                minString = p1.second + p2.second;
            }
        }
        return dp[key] = {currMin, "(" + minString + ")"};
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int p[n];
        for(int i = 0;i < n;i++)
            cin>>p[i];
        
        Solution ob;
        cout<<ob.matrixChainOrder(p, n)<<"\n";
    }
    return 0;
}  // } Driver Code Ends