/*
  We are given two integers n and k.You need to find the maximum values of x such that n!%k^x = 0.  

    INPUT :
        2
        5 2 
        1000 2
    OUTPUT :
        3
        994

*/

#include<bits/stdc++.h>
using namespace std;

int findMaxOfX(int n,int k){
    
    int ans = INT_MAX;
    long long p = 1;
    for (int i = 2;i*i<=k ; i++)
    {
        /* code */
        int cnt = 0;
        int occur = 0;
        if (k%i == 0)
        {
            /* code */
            p = i;

            while (k%i==0)
            {
                /* code */
                k = k/i;
                cnt++;
            }

            while (n/p)
            {
                /* code */
                occur += (n/p);
                p = p*i;

            }
            
            ans = min(ans,occur/cnt);
            
        }
        
    }

    if(k != 1){
        int p = k;
        int occur = 0;
        while (n/p)
        {
            /* code */
            occur += (n/p);
            p = p*k;
        }

        ans = min(ans,occur);
        
    }

    return ans;
    
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        int x = findMaxOfX(n,k);
        cout<<x<<endl;
    }
    
    return 0;
}