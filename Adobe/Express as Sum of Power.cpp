/*
	Adobe Question 5: Express as sum of power of natural numbers 

Given two numbers n and x, find out the total number of ways n can be 
expressed as sum of xth power of unique natural numbers.As total number 
of ways can be very large ,so return the number of ways modulo 109 + 7. 

*/


using namespace std;

 // } Driver Code Ends
//User function Template for C++
class Solution{
    public:
        int numOfWays(int n, int x)
    {
        long long dp[n + 1];
        const int M = 1e9 + 7;
        memset(dp, 0, sizeof(dp));
        dp[0] = dp[1] = 1;

        int range = pow(n, 1.0 / x);

        for (int i = 2; i <= range; i++)
        {

            int curr = pow(i, x);

            for (int j = n; j >= curr; j--)
            {
                dp[j] = (dp[j] + dp[j - curr]) % M;
            }
        }
        return dp[n];
    }
};



// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int  n, x;
        cin >> n >> x;
        Solution ob;
        cout<<ob.numOfWays(n, x)<<endl;
    }
    return 0;
}
  // } Driver Code Ends