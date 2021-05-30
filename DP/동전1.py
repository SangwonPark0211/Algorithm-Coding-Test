# https://www.acmicpc.net/problem/2293

coin = []
n, k = list(map(int, input().split()))
for _ in range(n):
    coin.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
# coin.sort()

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[-1])