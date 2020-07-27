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