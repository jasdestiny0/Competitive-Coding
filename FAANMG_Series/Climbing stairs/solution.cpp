#include<bits/stdc++.h>
#define N 10000
using namespace std;

int dp[N] = {0};

int noOfWays(int n){
	if(n<=0){
		return 0;
	}
	if(n==1 ){
		return dp[n] = 1;
	}
	if(n==2){
		return dp[n] = 2;
	}
	if(dp[n]!=0){
		return dp[n];
	}
	dp[n] = noOfWays(n-1)+noOfWays(n-2);
	return dp[n];
}


int main(){
	int n;
	cin>>n;
	int ans = noOfWays(n);
	cout<<ans<<endl;
	return 0;
}