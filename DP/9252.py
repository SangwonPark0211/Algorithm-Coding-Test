# https://www.acmicpc.net/problem/9252

s1 = input()
s2 = input()

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
for i in range(1, len(dp)):
    for j in range(1, len(dp[i])):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ""
cnt = dp[-1][-1]
i, j = len(s1), len(s2)
while cnt:
    if dp[i-1][j] == dp[i][j]-1 and dp[i][j-1] == dp[i][j]-1:
        cnt -= 1
        ans = s1[i-1] + ans
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
print(dp[-1][-1])
print(ans)