#encoding=utf-8
import numpy as np

def stock2(arr):
    L = len(arr)
    if L <= 1:
        return 0
    dp = np.zeros([L+1, 2])  #0表示当前不持股的最大收益，1表示当前持股的最大收益
    dp[0][0] = 0
    dp[0][1] = -arr[0]
    for i in range(1, L):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + arr[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - arr[i])
    return dp[L-1][0]


def greedy(arr):
    L = len(arr)
    if L <= 1:
        return 0
    result = 0
    for i in range(1, L):
        if arr[i] > arr[i-1]:
            result += arr[i] - arr[i-1]
    return result


if __name__ == '__main__':
    sample = [8,9,2,5,4,7,1]
    print(sample)
    result = greedy(sample)
    print(result)