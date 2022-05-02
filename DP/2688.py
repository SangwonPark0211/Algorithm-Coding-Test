# https://www.acmicpc.net/problem/2688

dp = [[0]*10 for _ in range(65)]
for i in range(10):
    dp[1][i] = 1
for i in range(2,65):
    for j in range(10):
        if j == 0:
            dp[i][j] = sum(dp[i-1])
        else:
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
for _ in range(int(input())):
    n = int(input())
    print(sum(dp[n]))

