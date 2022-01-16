/*
	Microsoft Question 11: Generate Binary Numbers 

Given a number N. The task is to generate and print all binary numbers 
with decimal values from 1 to N.

*/


using namespace std;

string toBinary(int num)
    {
        string binary;
        for(int i=31;i>=0;i--)
        {
            int bit = num>>i;
            if(bit&1) binary.push_back('1');
            else binary.push_back('0');
        }
        
        return binary.substr(binary.find('1'));
    }
vector<string> generate(int N)
{
	// Your code here
	vector<string>res;
	for(int i=1;i<=N;i++)
	{
	    res.push_back(toBinary(i));
	}
	
	return res;
	
}


// { Driver Code Starts.

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		vector<string> ans = generate(n);
		for(auto it:ans) cout<<it<<" ";
		cout<<endl;
	}
	return 0;
}  // } Driver Code Ends