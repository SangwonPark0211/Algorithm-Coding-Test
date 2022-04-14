# https://www.acmicpc.net/problem/2096

import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

lmax, cmax, rmax = dp[0][0], dp[0][1], dp[0][2]
lmin, cmin, rmin = dp[0][0], dp[0][1], dp[0][2]

for i in range(1, N):
    lmax, cmax, rmax = max(lmax, cmax) + dp[i][0], max(lmax, cmax, rmax) + dp[i][1], max(cmax, rmax) + dp[i][2]
    lmin, cmin, rmin = min(lmin, cmin) + dp[i][0], min(lmin, cmin, rmin) + dp[i][1], min(cmin, rmin) + dp[i][2]

print(max(lmax, cmax, rmax), min(lmin, cmin, rmin))