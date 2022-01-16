/*
	Microsoft Question 10: Stickler Thief

Stickler the thief wants to loot money from a society having n houses in a single line. He is a 
weird person and follows a certain rule when looting the houses. According to the rule, he will 
never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. 
The thief knows which house has what amount of money but is unable to come up with an optimal 
looting strategy. He asks for your help to find the maximum money he can get if he strictly 
follows the rule. Each house has a[i]amount of money present in it.


*/
using namespace std;
typedef long long int ll;

 // } Driver Code Ends
class Solution
{
    public:
    //Function to find the maximum money the thief can get.
    int FindMaxSum(int arr[], int n)
    {
        if(n==0) return 0;
        if(n==1) return arr[0];
       
        int v1 = arr[0];
        int v2 = max(v1, arr[1]);
       
        for(int i=2; i<n; i++){
           int temp = v2;
           v2 = max(v2, v1+arr[i]);
           v1 = temp;
        }
       
        return v2;
    }
};

// { Driver Code Starts.
int main()
{
    //taking total testcases
	int t;
	cin>>t;
	while(t--)
	{
	    //taking number of houses
		int n;
		cin>>n;
		int a[n];
		
		//inserting money of each house in the array
		for(int i=0;i<n;++i)
			cin>>a[i];
		Solution ob;
		//calling function FindMaxSum()
		cout<<ob.FindMaxSum(a,n)<<endl;
	}
	return 0;
}
  // } Driver Code Ends