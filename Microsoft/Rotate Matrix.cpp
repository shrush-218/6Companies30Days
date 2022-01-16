/*
	Microsoft Question 3: Rotate by 90 degrees

Given a square matrix[][] of size N x N. The task is to rotate it by 90 
degrees in an anti-clockwise direction without using any extra space.

*/

// { Driver Code Starts

using namespace std;
void rotate(vector<vector<int> >& matrix);


 // } Driver Code Ends
//User function template for C++

/* matrix : given input matrix, you are require 
 to change it in place without using extra space */
void rotate(vector<vector<int>> &mat)
{
    int n = mat.size();
    
    for(int i = 0; i < n; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            swap(mat[i][j], mat[j][i]);
        }
    }
    
    for(int i; i < n/2; i++)
    {
        for(int j = 0; j < n; j++)
        {
            swap(mat[i][j], mat[n-1-i][j]);
        }
    }
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
        vector<vector<int> > matrix(n);
        for(int i=0; i<n; i++)
        {
            matrix[i].resize(n);
            for(int j=0; j<n; j++)
                cin>>matrix[i][j]; 
        }
        rotate(matrix);
        for (int i = 0; i < n; ++i)
        {
            for(int j=0; j<n; j++)
                cout<<matrix[i][j]<<" ";
            cout<<"\n";
        }
    }
    return 0;
}

  // } Driver Code Ends