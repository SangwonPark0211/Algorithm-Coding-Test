# https://www.acmicpc.net/problem/2407

dp = [1]*101
for i in range(2, 101):
    dp[i] = dp[i-1] * i

n, m = map(int, input().split())
up = dp[n]
down = dp[n-m] * dp[m]
print(up//down)