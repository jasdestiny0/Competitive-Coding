/*
So,your task is to print the number of palindromic substring in the given string.
A string is called palindrome if its reverse is equal to the string itself eg. "aba"
The substrings with different start indexes or end indexes are counted as different substrings even if they consist of same characters.

Input Format
The first and the only line of input contains a string s.

Constraints
1<=|s|<=10^4 where |s| is the length of the given string.

Output Format
Print a single integer equal to number of palindromic substring in the given string.

Sample Input
abcde
Sample Output
5
Explanation
The only palindromic substring are of length 1.So,the answer is 5('a', 'b', 'c', 'd' and 'e')
*/
#include <bits/stdc++.h>
using namespace std;
bool dp[10001][10001] = {0};

int noOfPalindromicSubstring(string s){
    int n = s.length();
    for(int i=0;i<n;i++){
        dp[i][i] = true;
    }

    for(int i=0;i<n-1;i++){
        if(s[i]==s[i+1]){
            dp[i][i+1] = true;
        }
    }

    for(int d=2;d<n;d++){
        int i=0,j=d;
        while(j<n){
            if((s[i]==s[j])&&(dp[i+1][j-1]==true)){
                dp[i][j] = true;
            }
            i++;
            j++;
        }
    }

    int ans = 0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(dp[i][j]==true){
                ans++;
            }
        }
    }
    return ans;




}


int main(){
    string s;
    cin>>s;
    int ans =  noOfPalindromicSubstring(s);
    cout<<ans<<endl;
    return 0;
}
