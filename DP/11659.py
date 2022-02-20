# https://www.acmicpc.net/problem/11659
import sys

N, M = map(int, sys.stdin.readline().split())
dp = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(2,len(dp)):
    dp[i] += dp[i-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j]-dp[i-1])