/*
We are given an array containg n numbers. All the numbers are present twice except for two numbers which are present only once. Find the unique numbers in linear time without using any extra space. ( Hint - Use Bitwise )

Input Format
First line contains the number n. Second line contains n space separated number.

Constraints
n < 10^5

Output Format
Output a single line containing the unique numbers separated by space

Sample Input
4
3 1 2 1
Sample Output
2 3
Explanation
Smaller number comes before larger number
*/

#include<bits/stdc++.h>
using namespace std;

void findTwoUniqueNumbers(vector<int> v){
    int a,b,c = v[0];
    for(int i = 1;i <v.size();i++){
        c = c^v[i];
    }
    int mask = 1;
    while(true){
        if((c&mask)==0){
            mask = mask<<1;
        }
        else{
            break;
        }
    }
 
    b = 0;
    for (int i = 0; i < v.size(); i++)
    {
        /* code */
        if((mask&v[i])!=0){
            b ^= v[i];
        }

    }
    a = c^b;
    cout<<min(a,b)<<" "<<max(a,b)<<endl;

    
}


int main(){
    int n,x;
    cin>>n;
    vector<int> v(n);
    for(int i=0;i<n;i++){
        cin>>x;
        v[i] = x;
    }
    findTwoUniqueNumbers(v);
    return 0;
}
