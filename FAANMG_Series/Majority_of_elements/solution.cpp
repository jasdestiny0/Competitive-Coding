/*
You have to given an array A of size N.
Find all the elements which appear more than floor(N/3) times in the given array.
Wait Wait!
There is a condition that you have to do your job in O(N) time complexity and O(1) space complexity.

Input Format
First line contains N ->No. of elements in the array
Second line has N integers denoting the elements of the array A ie A1,A2,A3…….AN.

Constraints
1<=N<=10^7
0<=Ai<=10^9

Output Format
Print a single line containing all the majority elements occurring more than floor(N/3) times.
If there is no majority element then just print "No Majority Elements".

Sample Input
8
2 2 3 1 3 2 1 1 
Sample Output
1 2
*/


#include<bits/stdc++.h>
#define ll long long
using namespace std;

void findMajority(vector<ll> arr,ll n){
    ll floor = n/3;
    ll count1 = 0,count2 = 0;
    ll ele1 = -1,ele2 = -1;
    for(ll i=0;i<n;i++){
        if(arr[i] == ele1){
            count1++;
        }
        else if(arr[i] == ele2){
            count2++;
        }
        else if(count1 == 0){
            ele1 = arr[i];
            count1 = 1;
        }
        else if(count2 == 0){
            ele2 = arr[i];
            count2 = 1;
        }
        else{
            count1--;
            count2--;
        }
    }

    count1 = count2 = 0;
    for(ll i=0;i<n;i++){
        if(arr[i] == ele1){
            count1++;
        }
        else if(arr[i] == ele2){
            count2++;
        }
    }


    if(count1>floor){
        cout<<ele1<<" ";
    }
    if(count2>floor){
        cout<<ele2<<endl;
    }
    if(count1<=floor && count2<=floor){
        cout<<"No Majority Elements";
    }
}

int main(){
    ll n;
    cin>>n;
    vector<ll> arr;
    for (ll i = 0; i < n; i++)
    {
        /* code */
        ll x;
        cin>>x;
        arr.push_back(x);
    }
    findMajority(arr,n);
    
    return 0;
}