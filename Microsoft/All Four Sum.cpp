/*
	Microsoft Question 12: Find All Four Sum Numbers 

Given an array of integers and another number. Find all the unique quadruple 
from the given array that sums up to the given number.

*/
// { Driver Code Starts

using namespace std;

 // } Driver Code Ends
// User function template for C++

class Solution{
    public:
    vector<vector<int> > fourSum(vector<int> &arr, int k) {
        // Your code goes here
        vector<vector<int>> ans;
        if(arr.empty()) return ans;
        int n=arr.size();
        sort(arr.begin(),arr.end());
        
        for(int i=0;i<n; i++){
            for(int j=i+1;j<n;j++){
                int temp_target=k-arr[i]-arr[j];
                int front=j+1;
                int back=n-1;
                
                while(front<back){
                    int pair_sum=arr[front]+arr[back];
                    if(pair_sum<temp_target) front++;
                    else if(pair_sum > temp_target) back--;
                    else{
                        vector<int> unique(4,0);
                        unique[0]=arr[i];
                        unique[1]=arr[j];
                        unique[2]=arr[front];
                        unique[3]=arr[back];
                        ans.push_back(unique);
                        
                        //processing the duplicates of number 3
                        while(front<back && arr[front]==unique[2]) front++;
                        //processing the duplicates of number 4
                        while(front<back && arr[back]==unique[3]) --back;
                    }
                }
            
            while(j+1<n && arr[j+1]==arr[j]) j++;
            //processing the duplicates of number 2.
                
            }
            while(i+1<n && arr[i+1]==arr[i]) i++;
        }
        return ans;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k, i;
        cin >> n >> k;
        vector<int> a(n);
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        vector<vector<int> > ans = ob.fourSum(a, k);
        for (auto &v : ans) {
            for (int &u : v) {
                cout << u << " ";
            }
            cout << "$";
        }
        if (ans.empty()) {
            cout << -1;
        }
        cout << "\n";
    }
    return 0;
}  // } Driver Code Ends