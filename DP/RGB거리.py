# https://www.acmicpc.net/problem/1149
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0,0,0] for _ in range(n)]
for i in range(3):
    dp[0][i] = arr[0][i]
for i in range(1, n):
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
print(min(dp[-1]))