# https://www.acmicpc.net/problem/11053

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))