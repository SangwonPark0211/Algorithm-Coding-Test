# https://www.acmicpc.net/problem/10164

N, M, K = map(int, input().split())
dp = [[0 for _ in range(M)] for _ in range(N)]
for i in range(M):
    dp[0][i] = 1
for i in range(N):
    dp[i][0] = 1

# K = 0인 경우
if K == 0:
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

# K != 0인 경우
elif K != 0:
    if K%M == 0:
        row = K//M-1
        col = M - 1
    else:
        row = K//M
        col = K%M - 1
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(row+1, N):
        dp[i][col] = dp[row][col]
    for i in range(col+1, M):
        dp[row][i] = dp[row][col]
    for i in range(row + 1, N):
        for j in range(col + 1, M):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
# for i in range(len(dp)):
#     print(dp[i])
print(dp[-1][-1])