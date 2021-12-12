#include <iostream>

using namespace std;

int dp_func(int* arr, int k)
{
    int dp[3][k+1];
    memset(dp, 0, sizeof(dp));
    int tmp = 0;
    for(int i=1; i<=k; i++) {
        tmp = arr[i-1] % 3;
        if (tmp == 0) {
            dp[0][i] = dp[0][i-1] + arr[i-1];
            dp[1][i] = dp[1][i-1] > 0 ? dp[1][i-1] + arr[i-1] : dp[1][i-1];
            dp[2][i] = dp[2][i-1] > 0 ? dp[2][i-1] + arr[i-1] : dp[2][i-1];
        } else if (tmp == 1) {
            dp[0][i] = dp[2][i-1] > 0 ? dp[2][i-1] + arr[i-1] : dp[0][i-1];
            dp[1][i] = dp[0][i-1] > 0 ? dp[0][i-1] + arr[i-1] : arr[i-1];
            dp[2][i] = dp[1][i-1] > 0 ? dp[1][i-1] + arr[i-1] : dp[2][i-1];
        } else {
            dp[0][i] = dp[1][i-1] > 0 ? dp[1][i-1] + arr[i-1] : dp[0][i-1];
            dp[1][i] = dp[2][i-1] > 0 ? dp[2][i-1] + arr[i-1] : dp[1][i-1];
            dp[2][i] = dp[0][i-1] > 0 ? dp[0][i-1] + arr[i-1] : arr[i-1];
        }
    }
    return dp[0][k];
}

int greedy_func(int* arr, int k) 
{
    int sum = 0;
    int tmp = 0;
    int a1 = 2<<20; int a2 = 2<<20; int b1 = 2<<20; int b2 = 2<<20;
    for (int i=0; i<k; i++){
        sum += arr[i];
        tmp = arr[i] % 3;
        if (tmp == 1) {
            if (arr[i] < a1) {
                a1 = arr[i]; 
            } else if (arr[i] < a2) {
                a2 = arr[i];
            }
        } else if (tmp == 2) {
            if (arr[i] < b1) {
                b1 = arr[i]; 
            } else if (arr[i] < b2) {
                b2 = arr[i];
            }
        }
    }
    tmp = sum % 3;
    if (tmp == 0) {
        return sum;
    } else if (tmp == 1) {
        return max(0, max(sum - a1, sum - b1 - b2));
    } else {
        return max(0, max(sum - a1 - a2, sum - b1));
    }
}

int main()
{
    int a[5] = {3,6,5,1,8};
    cout << dp_func(a, 5) << endl;
    cout << greedy_func(a, 5) << endl;
    int b[1] = {4};
    cout << dp_func(b, 1) << endl;
    cout << greedy_func(b, 1) << endl;
    return 0;
}