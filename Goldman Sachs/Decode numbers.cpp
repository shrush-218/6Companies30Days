'''
	Goldman Sachs Question 8: Total Decoding Messages

A top secret message containing letters from A-Z is being encoded to 
numbers using the following mapping:

A -> 1
B -> 2
...
Z -> 26
You are an FBI agent. You have to determine the total number of ways 
that message can be decoded, as the answer can be large return the 
answer modulo 109 + 7.
Note: An empty digit sequence is considered to have one decoding. It 
may be assumed that the input contains valid digits from 0 to 9 and If 
there are leading 0s, extra trailing 0s and two or more consecutive 
0s then it is an invalid string.
'''


// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
	public:
		int CountWays(string str){
		    int n=str.length();
        int dp[n+1];
        int mod = 1e9 + 7;
        dp[0]=1;
        dp[1]=1;
       
        if(n==1 && str[0]!='0')
        return 1;
        if(str[0]=='0')
        return 0;
        
        for(int i=2;i<=n;i++)
        {
            dp[i]=0;
            
            if(str[i-1]>'0')
            dp[i] = dp[i-1];
            
            if(str[i-2]=='1' || str[i-2]=='2' && str[i-1]<'7')
            dp[i] = (dp[i]+dp[i-2])%mod;
        }
        return dp[n];
    }		
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string str;
		cin >> str;
		Solution obj;
		int ans = obj.CountWays(str);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends