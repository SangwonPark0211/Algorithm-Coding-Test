# https://www.acmicpc.net/problem/11060
n = int(input())
arr = list(map(int, input().split()))

dp = [n] * n 
dp[0] = 0

for i in range(n-1):
    for j in range(1, arr[i]+1):
        if i+j >= n:
            break
        dp[i+j] = min(dp[i+j], 1+dp[i])

if dp[-1]==n:
    print(-1)
else:
    print(dp[-1])

