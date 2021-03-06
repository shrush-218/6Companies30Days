/*
	Intuit Question 2: Word Search 

Given a 2D board of letters and a word. Check if the word exists in the board. The 
word can be constructed from letters of adjacent cells only. ie - horizontal or 
vertical neighbors. The same letter cell can not be used more than once.

*/
// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution {
public:
    bool dfs(vector<vector<char>>& board,string word,int i,int j,int pos)
    {
        int m=board.size();
        int n=board[0].size();
        if(i<0 || j<0 || i>=m || j>=n)
        return false;
        if(pos==word.length())
        return true;
        if(word[pos]==board[i][j])
        {
            char temp=board[i][j];
            board[i][j]='#';
            bool a=dfs(board,word,i+1,j,pos+1); 
            bool b=dfs(board,word,i-1,j,pos+1);
            bool c=dfs(board,word,i,j+1,pos+1);
            bool d=dfs(board,word,i,j-1,pos+1);
            board[i][j]=temp;
            return a||b||c||d;
        }
        else
        return false;
        
    }
    bool isWordExist(vector<vector<char>>& board, string word) {
        int m=board.size();
        int n=board[0].size();
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(board[i][j]==word[0])
                {
                    if(dfs(board,word,i,j,0))
                    return true;
                }
            }
        }
        return false;
    }
};
// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<char>>board(n, vector<char>(m, '*'));
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> board[i][j];
		string word;
		cin >> word;
		Solution obj;
		bool ans = obj.isWordExist(board, word);
		if(ans)
			cout << "1\n";
		else cout << "0\n";
	}
	return 0;
}  // } Driver Code Ends