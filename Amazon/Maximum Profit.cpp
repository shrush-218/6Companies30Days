'''
	Amazon Question 1: Maximum Profit

In the stock market, a person buys a stock and sells it on some 
future date. Given the stock prices of N days in an array A[ ] and 
a positive integer K, find out the maximum profit a person can make 
in at-most K transactions. A transaction is equivalent to (buying + 
selling) of a stock and new transaction can start only when the 
previous transaction has been completed.

'''

// { Driver Code Starts
// Initial template for C++

using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int maxProfit(int K, int N, int A[]) {
        int dp[K+1][N];
        memset(dp,0,sizeof(dp));
        for(int i=1; i<=K;i++)
        {
            int mx=INT_MIN;
            for(int j=1;j<N;j++)
            {
                mx=max(mx,dp[i-1][j-1]-A[j-1]);
                dp[i][j]=max(dp[i][j-1],mx+A[j]);
            }
        }
        return dp[K][N-1];
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin >> K;
        cin >> N;
        int A[N];
        for (int i = 0; i < N; i++) cin >> A[i];

        Solution ob;
        cout << ob.maxProfit(K, N, A) << endl;
    }
    return 0;
}  // } Driver Code Ends