#include<bits/stdc++.h>
using namespace std;
map<int,int> dp;
// In this problem we have three cases
// n reaching 1
// n not reaching 1 and forming loop
// n reaching infinity(actually this case is not possible and thats y this question is tricky)
bool overHappyNumbers(int n){
	if(n==1){
		return true;
	}
	if(dp.count(n)!=0){
		return false;
	}
	dp[n] = 1;
	int sum = 0,x;
	while(n>0){
		x = n%10;
		sum += (x*x);
		n = n/10;
	}
	return overHappyNumbers(sum);
}

int main(){
	int n;
	cin>>n;
	bool ans = overHappyNumbers(n);
	if(ans == true) cout<<"true"<<endl;
	else cout<<"false"<<endl;
	return 0;
}