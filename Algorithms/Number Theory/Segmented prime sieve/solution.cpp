#include<bits/stdc++.h>
#include<memory>
using namespace std;

const int N = 100000;
vector<int> primes; // To store all the prime numbers between 1 to N
int p[N] = {0};

void sieve(){
    for(int i=3;i<N;i+=2){
        p[i] = 1;
    }
    p[2] = 1; 
    for(int i=0;i<N;i++){
        if(p[i]==1){
            primes.push_back(i);
            for(int j=i*i;j<N;j+=i){
                p[j] = 0;
            }
        }
    }
}

int main(){

    sieve(); //Build once
    int t;
    cin>>t;
    while (t--)
    {
        int n,m;
        cin>>m>>n;
        bool segement[n-m+1];
        int size = n-m+1;
        memset(segement,0,size);

        for(auto x:primes){

            if(x*x>n){
                break;
            }

            int start = (m/x)*x;
            
            if(x>=m && x<=n){
                start = 2*x;
            }

            if(start<m){
                start+=x;
            }
            
            for(int i=start;i<=n;i+=x){
                segement[i-m] = 1;
            }
        }

        for(int i=m;i<=n;i++){
            if(segement[i-m]==0 && i!=1){
                cout<<i<<endl;
            }
        }
    }
    


}
