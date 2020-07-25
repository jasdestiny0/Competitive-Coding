#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	ll n,x;
	cin>>n;
	ll sum = 0;
	for(ll i=0;i<n;i++){
		cin>>x;
		sum += x;
	}
	ll total = (n*(n+1)/2);
	if(total - sum ==0){
		cout<<0<<endl;
	}
	else{
		cout<<total-sum<<endl;
	}
	return 0;
}