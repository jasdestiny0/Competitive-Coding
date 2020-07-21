#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;


vector<string> v;

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
    if((s.length()+v[i].length()<=26){
        s1 = strcat(s,v[i]);
        int h = findMaxLengthSubsequence(i+1,n,s1);
        int v = findMaxLengthSubsequence(i+1,n,s);
        return max(h,v);

    }
    else{
        return findMaxLengthSubsequence(i+1,n,s)
    }

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