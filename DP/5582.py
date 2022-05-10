# https://www.acmicpc.net/problem/5582
import sys
input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()
l1 = len(s1)
l2 = len(s2)

ans = 0
dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)