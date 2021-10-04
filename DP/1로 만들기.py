x = int(input())
dp = [0] * (10**6 + 1)
dp[1], dp[2], dp[3] = 0, 1, 1
if x==1:
    print(0)
elif x==2 or x==3:
    print(1)
else:
    for i in range(4,x+1):
        if i%2==0 and i%3==0:
            dp[i] = min(dp[i-1], min(dp[i//2], dp[i//3])) + 1
        elif i%2==0:
            dp[i] = min(dp[i-1], dp[i//2]) + 1
        elif i%3==0:
            dp[i] = min(dp[i-1], dp[i//3]) + 1
        else:
            dp[i] = dp[i-1] + 1
    print(dp[x])

