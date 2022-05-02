# https://www.acmicpc.net/problem/1890
arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[n-1][n-1])
            break
        cur_cnt = arr[i][j]
        if i + cur_cnt < n:
            dp[i+cur_cnt][j] += dp[i][j]
        if j + cur_cnt < n:
            dp[i][j+cur_cnt] += dp[i][j]
