'''
	Microsoft Question 14: Minimum steps to destination 

Given an infinite number line. You start at 0 and can go either to the left or 
to the right. The condition is that in the ith move, youmust take i steps. Given a 
destination D , find the minimum number of steps required to reach that destination.

'''
// { Driver Code Starts
// Initial Template for C++


using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int minSteps(int D){
        // code here
        int steps = 0, sum = 0;
        while(true){
            sum = sum + steps;
            steps++;
            if(sum == D){
                return steps-1;
                break;
            }
            if(sum > D and (sum-D)%2 == 0){
                return steps-1;
                break;
            }
        }
        return 0;
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int D;
        cin>>D;
        
        Solution ob;
        cout<<ob.minSteps(D)<<"\n";
    }
    return 0;
}  // } Driver Code Ends