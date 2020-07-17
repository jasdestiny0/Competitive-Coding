#include<bits/stdc++.h>
using namespace std;

void findTwoUniqueNumbers(vector<int> v){
    int a,b,c = v[0];
    for(int i = 1;i <v.size();i++){
        c = c^v[i];
    }
    int mask = 1;
    while(true){
        if((c&mask)==0){
            mask = mask<<1;
        }
        else{
            break;
        }
    }
 
    b = 0;
    for (int i = 0; i < v.size(); i++)
    {
        /* code */
        if((mask&v[i])!=0){
            b ^= v[i];
        }

    }
    a = c^b;
    cout<<min(a,b)<<" "<<max(a,b)<<endl;

    
}


int main(){
    int n,x;
    cin>>n;
    vector<int> v(n);
    for(int i=0;i<n;i++){
        cin>>x;
        v[i] = x;
    }
    findTwoUniqueNumbers(v);
    return 0;
}