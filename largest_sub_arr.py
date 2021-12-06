#encoding=utf-8
import numpy as np


def largest_sub_arr(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    dp = [0] * (len(arr) + 1)
    dp[0] = arr[0]
    L = len(arr)
    for i in range(1, L):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    return max(dp)

def largest_sub_arr2(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    L = len(arr)
    max_sub_sum = 0
    sub_sum = arr[0]
    for i in range(1, L):
        if sub_sum < 0:
            sub_sum = arr[i]
        else:
            sub_sum += arr[i]
        max_sub_sum = max(max_sub_sum, sub_sum)
    return max_sub_sum

if __name__ == '__main__':
    sample = [1, -5, 8, 3, -4, 15, -8]
    print(sample)
    result = largest_sub_arr2(sample)
    print(result)