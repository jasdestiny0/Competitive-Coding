/*
Ramu has an array of strings. He want to find a string s such that it is a concatenation of sub-sequence of given array and have unique characters.Since,he has just started coding so he needs your help.
A sub-sequence of an array is a set of elements that can be obtained by deleting some elements(posssibly none) from the array and keeping the order same.
Print the maximum possible length of s.

Input Format
The first line of input contains an interger n -the length of array.Next n lines contains the element(strings) of the array

Constraints
1 <= n <= 18, 1 <= arr[i].length<= 26

Output Format
Print one integer - the maximum length of s.

Sample Input
3
ab
cd
ab
Sample Output
4
*/
#include<bits/stdc++.h>
using namespace std;


vector<string> v;
vector<int> ans;

int findMaxLengthSubsequence(int i,int n,string s){
    if(i==n){
        int freq[100];
        memset(freq,0,sizeof(freq));
        for(int j=0;j<s.length();j++){
            int index = s[j] - 'a';
            if (freq[index]==0)
            {
                /* code */
                freq[index]+=1;
            }
            else
            {
                return 0;
            }
        }
        return s.length();
    }
    int h=-1,k=-1;
    if((s.length()+v[i].length()<=26)){
        h = findMaxLengthSubsequence(i+1,n,s+v[i]);

    }
    k = findMaxLengthSubsequence(i+1,n,s);
    return max(h,k);

}

int main(){
    int n;
    string x;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        /* code */
        cin>>x;
        v.push_back(x);
    }

    int ans = findMaxLengthSubsequence(0,n,"");
    cout<<ans<<endl;    
    return 0;
}
