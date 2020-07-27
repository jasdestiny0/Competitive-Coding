/*
Given a list of processes where each process have a unique id and a unique parent id . Parent id is the id of the process that initiated that process . You want to kill a particular process given by an integer kill . Print id of all the processes that will be killed to kill that process.You should print them in sorted order by id.
In order to kill a process , all its child processes should be killed as well . Also, only one process have parent id as 0 ie. that process started itself.

Input Format
The first line contains two integer - n (number of process ) and k (id of process to be killed).
Next line contains n integer equal to id of ith process.
Last line contains n integer equal to parent id of ith process.

Constraints
1<=n<=10^5

Output Format
Print id of all the process that will be killed in sorted order.

Sample Input
3 2
1 2 3
0 1 1
Sample Output
2
Explanation
Since , process with id 2 have no child , so it will only be killed.
*/

#include<bits/stdc++.h>
using namespace std;

vector<int> ans;

class Graph{
    map<int,list<int>> adjList;
    public:

        void addEdge(int u,int v,bool bidir = false){
            adjList[u].push_back(v);
            if(bidir){
                adjList[v].push_back(u);
            }
        }

        void dfs(int src){
            map<int,bool> visited;
            dfsHelper(src,visited);
        }

        void dfsHelper(int node,map<int,bool> &visited){
            visited[node] = true;
            ans.push_back(node);
            for(auto neighbour:adjList[node]){
                if(!visited[neighbour]){
                    dfsHelper(neighbour,visited);
                }
            }
        }
};

int main(){
    int n,k;
    cin>>n>>k;
    vector<int> id;
    vector<int> parent_id;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        id.push_back(x);
    }
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        parent_id.push_back(x);
    }
    Graph g;
    for(int i=0;i<n;i++){
        g.addEdge(parent_id[i],id[i]);
    }

    g.dfs(k);
    sort(ans.begin(),ans.end());
    for(auto x: ans){
        cout<<x<<" ";
    }
    cout<<endl;
    return 0;
}
