#include<bits/stdc++.h>
using namespace std;

const int N = 10000;
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

int no_of_factors(int m){

    int i=0;
    int p = primes[0];
    int ans = 1;

    while (p*p<=m)
    {
        /* code */
        int cnt = 0;
        if (m%p==0)
        {
         
            /* code */
            while(m%p==0){
                m = m/p;
                cnt++;
            }
        }
        ans *= (cnt+1);
        i++;
        p = primes[i];
    }

    if(m!=1){
        ans *= (2);
    }
    

    return ans;
}


int main(){
    sieve();
    int t;
    cin>>t;

    while(t--){
        int no;
        cin>>no;
        int count = no_of_factors(no);
        cout<<count<<endl;
    }


    return 0;
}
