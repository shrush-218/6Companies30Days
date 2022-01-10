'''
	Amazon Question 15:  Delete N nodes after M nodes of a linked list 

Given a linked list, delete N nodes after skipping M nodes of a 
linked list until the last of the linked list.

'''
// { Driver Code Starts
using namespace std;
/* A linked list node */


struct Node
{
    int data;
    struct Node *next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};

struct Node *start = NULL;

/* Function to print nodes in a given linked list */
void printList(struct Node *node)
{
    while(node != NULL)
    {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
    
}

void insert(int n1)
{
    int n,value;
    n=n1;
    struct Node *temp;
    
    for(int i=0;i<n;i++)
    {
        cin>>value;
        if(i==0)
        {
            start = new Node(value);
            temp=start;
            continue;
        }
        else
        {
            temp->next = new Node(value);
            temp=temp->next;
        }
    }
}

 // } Driver Code Ends

class Solution
{
    public:
    void linkdelete(struct Node  *head, int M, int N)
    {
        while(head) {
            int tempM = M;
            while(head && --tempM) head = head -> next;
            int tempN = N;
            Node *prevNode = head;
            while(head && tempN--) head = head -> next;
            if(prevNode) {
                head = head ? head -> next : NULL;
                prevNode -> next = head;
            }
        }
    }
};



// { Driver Code Starts.
int main()
{
    int t,n1;
    cin>>t;
    while (t--) {
        cin>>n1;
        int m,n;
        cin>>m;
        cin>>n;
        insert(n1);
        Solution ob;
        ob.linkdelete(start,m,n);
        printList(start);
    }
    
    return 0;
}
  // } Driver Code Ends