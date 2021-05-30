# https://www.acmicpc.net/problem/10844

n = int(input())
dp = [[1]*10 for _ in range(n)]
dp[0][0] = 0
for i in range(1,n):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
print(sum(dp[-1]) % 1000000000)