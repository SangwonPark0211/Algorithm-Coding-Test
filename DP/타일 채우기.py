# https://www.acmicpc.net/problem/2133

n = int(input())
dp = [0]*31
dp[0]=1
if n%2==1:
    print(0)
else:
    dp[2]=3
    dp[4]=11
    for i in range(6,31,2):
        dp[i] += dp[i-2]*3
        for j in range(4,i+1,2):
            dp[i] += dp[i-j] * 2
    print(dp[n])