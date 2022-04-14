# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [[0]*(N+1)]
for _ in range(N):
    dp.append([0] + list(map(int, input().strip().split())))
target = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    target.append([x1, y1, x2, y2])

# row accumulation
for i in range(1, N+1):
    for j in range(2,N+1):
        dp[i][j] += dp[i][j-1]
# col accumulation
for i in range(1, N+1):
    for j in range(2, N+1):
        dp[j][i] += dp[j-1][i]

for x1, y1, x2, y2 in target:
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

