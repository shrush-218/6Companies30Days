'''
	Amazon Question 5:  Phone Directory

Given a list of contacts contact[] of length n where each contact is a string 
which exist in a phone directory and a query string s. The task is to implement a 
search query for the phone directory. Run a search query for each prefix p of the 
query string s (i.e. from  index 1 to |s|) that prints all the distinct contacts 
which have the same prefix as p in lexicographical increasing order. Please refer 
the explanation part for better understanding.
Note: If there is no match between query and contacts, print "0".

'''

// { Driver Code Starts
// Initial Template for C++

using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    vector<vector<string>> displayContacts(int n, string contact[], string s)
    {
         vector<vector<string>> vec;

       set<string> st; 
       string search_str;

       search_str = s.substr(0,1); // first char of s
       
       // first of all search all strings in list with first char matching
       // and store the results lexicographicaly using a set of strings
       // then push the set values in a vector temp and push this temp       vector into a 2d vector vec
       // TC here -> O(n * max|contack[i]| * logn)
       
        for(int j=0; j<n; ++j)
         {
           if(contact[j].substr(0,1) == search_str)
           {
             st.insert(contact[j]); // insert into set
           }
         }
         
          vector<string> temp;
           
         if(!st.empty())  // push set values in vec
         {
          for(auto it: st)
          {
            temp.push_back(it);
          }
           vec.push_back(temp);
         }
         else    // if no value found then we have to push zero in whole vec                    //and return it
         {
         temp.push_back("0");
         for(int d = 0; d<s.size(); ++d)
         {
           vec.push_back(temp);
         }
         return vec;
         }

         
  // Now we have vec with 1st row , rest s.size()-1 rows can be found by 
  // searching for next substrings in previous rows 
  // like searching in vec[0]th vector to fill vec[1] and in vec[1] to fill vec[2] and so on
  // TC here -> O(|s| * n)
  
       for(int i=1; i<s.size(); ++i)
       { 
         temp.clear();
         search_str = s.substr(0, i+1);

         for(int j = 0; j<vec[i-1].size(); ++j)
         {
            if(vec[i-1][j].substr(0,i+1) == search_str)
            {
              temp.push_back(vec[i-1][j]);
            }
         }

         if(temp.size() == 0)
         { 
           temp.push_back("0"); 
           while(i<s.size())
           {
             vec.push_back(temp);
             i++;
           }
           return vec;
         }
         else
         vec.push_back(temp);
         

         }

       return vec;
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string contact[n], s;
        for(int i = 0;i < n;i++)
            cin>>contact[i];
        cin>>s;
        
        Solution ob;
        vector<vector<string>> ans = ob.displayContacts(n, contact, s);
        for(int i = 0;i < s.size();i++){
            for(auto u: ans[i])
                cout<<u<<" ";
            cout<<"\n";
        }
    }
    return 0;
}  // } Driver Code Ends