/*
Question link : https://codeforces.com/problemset/problem/1294/C
*/

#include<bits/stdc++.h>
#define ll long long
using namespace std;

void findAns(ll n){
    ll n_copy = n;
    vector<pair<ll,ll>> count;
        ll total_size = 0;
        for(ll i=2;i*i<=n;i++){
            ll cnt=0;
            if(n%i==0){
                while(n%i==0){
                    cnt++;
                    n = n/i;
                }
                count.push_back(make_pair(i,cnt));
                total_size++;
            }
        }
        if(n!=1){
            count.push_back(make_pair(n,1));
            total_size++;
        }
        ll a,b,c = 1;
        if(total_size>=3){
            
            a = pow(count[0].first,count[0].second);
            b = pow(count[1].first,count[1].second);
            for (ll i = 2; i < count.size(); i++)
            {
                /* code */
                c = c*pow(count[i].first,count[i].second);
            }
            cout<<"YES"<<endl;
            cout<<a<<" "<<b<<" "<<c<<endl;
            return;

        }
        if(total_size==2){
            ll sol_exists = 0;
            a = count[0].first;
            b = count[1].first;
            c = n_copy/(a*b);
            if(c!=a && c!=b && c!=1){
                cout<<"YES"<<endl;
                cout<<a<<" "<<b<<" "<<c<<endl;
                return;
            }
            else{
                cout<<"NO"<<endl;
            }
        }
        else{
            if(count[0].second>=6){
                a = count[0].first;
                b = pow(count[0].first,2);
                c = pow(count[0].first,count[0].second-3);
                cout<<"YES"<<endl;
                cout<<a<<" "<<b<<" "<<c<<endl;
                return;
            }
            else{
                cout<<"NO"<<endl;
                return;
            }
        }
        return;

}

int main(){
    ll t;
    cin>>t;
    while (t--)
    {
        /* code */
        ll n,total_size = 0;
        cin>>n;
        
        findAns(n);

    }
    
    return 0;
}
