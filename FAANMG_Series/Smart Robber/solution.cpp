#include<bits/stdc++.h>
using namespace std;

int dp[10000];

int maxMoney(vector<int> v,int i){
	if(i<0){
		return 0;
	}
	if(dp[i]!=0){
		return dp[i];
	}
	int a  = INT_MIN, b = INT_MIN;
	a = maxMoney(v,i-2)+v[i];
	b = maxMoney(v,i-1);
	return dp[i] = max(a,b);


}

int main(){
	int t;
	cin>>t;
	while(t--){
		int n,x;
		cin>>n;
		vector<int> v;
		for(int i=0;i<n;i++){
			cin>>x;
			v.push_back(x);
		}
		memset(dp,0,sizeof(dp));
		int ans = maxMoney(v,n-1);
		cout<<ans<<endl;
	}
	return 0;
}