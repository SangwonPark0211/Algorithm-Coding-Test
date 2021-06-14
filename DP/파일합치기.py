# https://www.acmicpc.net/problem/11066

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cumsum = {-1:0}
    for i in range(n):
        cumsum[i] = cumsum[i-1] + arr[i]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # initialization
    for gap in range(1, n):
        for start in range(n):
            end = start + gap
            if end == n:
                break
            dp[start][end] = float('inf')
            for i in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][i] + dp[i+1][end] + cumsum[end] - cumsum[start-1])
    
    # for i in range(n):
    #     print(dp[i])
    print(dp[0][-1])


