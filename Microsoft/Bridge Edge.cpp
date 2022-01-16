/*
	Microsoft Question 13: Bridge edge in a graph 

Given a Graph of V vertices and E edges and another edge(c - d), the task is 
to find if the given edge is a Bridge. i.e., removing the edge disconnects the graph.

*/

// { Driver Code Starts

using namespace std;

 // } Driver Code Ends
class Solution
{
	private:
    int find_(vector<int>& p, int v) {
        if(p[v] == -1) return v;
        else return p[v] = find_(p, p[v]);
    }
    
    void union_(vector<int>& p, vector<int>& r, int u, int v) {
        int pu = find_(p, u);
        int pv = find_(p, v);
        if(pu == pv) return;
        else {
            if(r[pu] == r[pv]) {
                p[pu] = pv;
                r[pv]++;
            }
            else if(r[pu] < r[pv]) p[pu] = pv;
            else p[pv] = pu;
        }
    }
	
	public:
    //Function to find if the given edge is a bridge in graph.
    int isBridge(int V, vector<int> adj[], int c, int d) 
    {
        vector<int> p(V, -1), r(V, 0);
        for(int u=0; u<V; u++) {
            for(int v : adj[u]) {
                if((u == c and v == d) or (u == d and v == c)) continue;
                union_(p, r, u, v);
            }
        }
        
        if(find_(p, c) != find_(p, d)) return 1;
        return 0;
        
    }
};

// { Driver Code Starts.


int main()
{
    int t;
    cin >> t;
    while (t--) {
        int V, E;
        cin >> V >> E;
        vector<int> adj[V];
        int i=0;
        while (i++<E) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back (v);
            adj[v].push_back (u);
        }
        
        int c,d;
        cin>>c>>d;
        
        Solution obj;
    	cout << obj.isBridge(V, adj, c, d) << "\n";
    }

    return 0;
}

  // } Driver Code Ends