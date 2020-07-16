/*
We have an array of positive integers. The task is to print the maximum length of Bitonic subsequence.
A bitonic sequence is any sequence which first increases in magnitude and then at a certain point it starts to decrease in magnitude.
For eg: 1 2 3 2 1 is a bitonic sequence while 1 2 3 2 1 2 3 is not, since it first increases, then decreases and then again increases.

Input Format
First line contains T test cases. Each test case has N , as number of elements in an array. Next line of every test consists of elements in array.

Constraints
1<=T<=100
1<=N<=100
1<=Ai<=200

Output Format
For each testcase , in a new line, print the length of longest Bitonic sequence.

Sample Input
2
9
1 3 5 7 4 3 5 2 6
11
4 5 6 3 2 7 8 5 4 6 3 
Sample Output
7
8
Explanation
In the first test case we can select numbers 1 3 5 7 4 3 2 => ans =7.
In the second testcase we can select numbers 4 5 6 7 8 5 4 3 => ans=8
*/

#include<bits/stdc++.h>
using namespace std;


int solve(vector<int> arr,int n){
    vector<int> left(n,1);
    vector<int> right(n,1);

    // left array
    for (int i = 1; i < n; i++)
    {
        /* code */
        for (int j = 0; j < i; j++)
        {
            /* code */
            if(arr[i]>arr[j]){
                left[i] = max(left[i],left[j]+1);
            }
        }
        
    }

    // Right array

    for (int i = n-2; i >=0; i--)
    {
        /* code */
        for (int j = i+1; j < n; j++)
        {
            /* code */
            if(arr[i]>arr[j]){
                right[i] = max(right[i],right[j]+1);
            }

        }
        
    }
    int max_length = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        /* code */
        int temp_max = right[i]+left[i]-1;
        max_length = max(temp_max,max_length);
    }    
    return max_length;
    
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++)
        {
            /* code */
            int x;
            cin>>x;
            arr[i] = x;
        }
        int max_length = solve(arr,n);
        cout<<max_length<<endl;
        
    }
    return 0;
}