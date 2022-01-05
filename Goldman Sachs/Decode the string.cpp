'''
	Goldman Sachs Question 13: Decode the String

An encoded string (s) is given, the task is to decode it. The pattern 
in which the strings were encoded were as follows
original string: abbbababbbababbbab 
encoded string : 3[a3[b]1[ab]]

'''

// { Driver Code Starts
// Initial Template for C++


using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    string decodedString(string s){
        string num = "";
        string ans="";
        int n;
        string temp="";
        string temp2="";
        stack<char> st;
        int p = 0;
        
        while(p<s.size())
        {    if(s[p]==']')
             {  while(st.top() != '[')
                {
                    temp=st.top()+temp;
                    st.pop();
                }
                 st.pop();
              while(isdigit(st.top()))
                {    num=st.top()+num;
                     st.pop();
                     if(st.empty()){
                         break;
                     }
                }
                n=stoi(num);
                for(int i=1;i<=n;i++)
                {   temp2=temp2+temp;
                }
                if(st.empty())
                {   ans=temp2;
                    break;
                }
                for(int i=0;i<temp2.size();i++)
                {    st.push(temp2[i]);
                }
                
                temp="";
                temp2="";
                num="";
            }
            else
            {    st.push(s[p]);
            }
            p++;
        }
        return ans;
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        
        Solution ob;
        cout<<ob.decodedString(s)<<"\n";
    }
    return 0;
}  // } Driver Code Ends