#include<bits/stdc++.h>
#define ll long long
using namespace std;



ll solve(int n,int c,vector<ll> stall_nos){

    ll range = stall_nos[n-1] - stall_nos[0];
    ll low = 1;
    ll high = range;
    ll gap = (low+high)/2;
    ll best = -1;

    while (low<=high)
    {
        /* code */ 
        
        int last_filled_stall_index = 0;       
        ll count = 1;

        for(int i=1;i<n && count<c;i++){
            ll last_filled_stall = stall_nos[last_filled_stall_index];
            ll current_stall = stall_nos[i];
            if ((current_stall - last_filled_stall)>=gap)
            {
                /* code */
                count++;
                last_filled_stall_index = i;

            }
            
        }
        if(count == c){
            best = gap;
            low = gap+1;
            gap = (low+high)/2;
        }
        else{
            high = gap-1;
            gap = (low+high)/2;
        }
       
        
    }
    return best;
    
}

int main(){
    int t;
    cin>>t;
    while (t--)
    {
        /* code */
        int n,c,x;
        cin>>n>>c;
        vector<ll> stall_nos;
        for (int i = 0; i < n; i++)
        {
            /* code */
            cin>>x;
            stall_nos.push_back(x);
        }
        sort(stall_nos.begin(),stall_nos.end());
        ll ans = solve(n,c,stall_nos);
        cout<<ans<<endl;

    }
    return 0;
}
