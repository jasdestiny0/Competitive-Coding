#include <bits/stdc++.h>
using namespace std;

int matrixChainMultiplication(int *arr, int n)
{

    int dp[100][100];
    memset(dp, 0, sizeof(dp));

    // To iterate the upper diagonal elements

    for (int i = 1; i < n; i++)
    {
        int r = 0, c = i;
        while (r < n)
        {
            int temp_cost = INT_MAX;

            for (int k = r; k < c; k++)
            {
                temp_cost = min(temp_cost, dp[r][k] + dp[k + 1][c] + (arr[r] * arr[k + 1] * arr[c + 1]));
            }

            dp[r][c] = temp_cost;

            r++, c++;
        }
    }

    return dp[0][n - 1];
}

int main()
{

    int n, arr[100];
    cin >> n;
    for (int i = 0; i < n + 1; i++)
    {
        cin >> arr[i];
    }

    int ans = matrixChainMultiplication(arr, n);

    cout << ans << endl;

    return 0;
}