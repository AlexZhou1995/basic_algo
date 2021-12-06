#encoding=utf-8
import numpy as np

def longestPalindromeSubseq(s):
    L = len(s)
    if L <= 1:
        return L
    dp = [[0]*L for i in range(L)] #dp[i][j]表示从i到j的最长子序列
    for i in range(L):
        dp[i][i] = 1
    for i in range(L-2, -1, -1):
        for j in range(i+1, L):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-2]+2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][L-1]

if __name__ == '__main__':
    sample = 'bbbab'
    result = longestPalindromeSubseq(sample)
    print(result)