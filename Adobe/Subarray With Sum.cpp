/*
	Adobe Question 1: Subarray with given sum 

Given an unsorted array A of size N that contains only non-negative 
integers, find a continuous sub-array which adds to a given number S.

*/
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(int arr[], int n, long long s)
    {
        // Your code here
        int i=0, j=0;
        long sum=0;
        while(j<=n){
            if(sum < s) sum+=arr[j++];
            else if(sum > s) sum-=arr[i++];
            else if(i<j) return {i+1, j};
            else sum+=arr[j++];
        }
        return {-1};
    }
};

// { Driver Code Starts.

int main()
 {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        long long s;
        cin>>n>>s;
        int arr[n];
        const int mx = 1e9;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        Solution ob;
        vector<int>res;
        res = ob.subarraySum(arr, n, s);
        
        for(int i = 0;i<res.size();i++)
            cout<<res[i]<<" ";
        cout<<endl;
        
    }
	return 0;
}  // } Driver Code Ends