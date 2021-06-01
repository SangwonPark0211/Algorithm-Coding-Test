# https://www.acmicpc.net/problem/9251
s1 = input()
s2 = input()
l1, l2 = len(s1), len(s2)
dp = [[0 for _ in range(l2)] for _ in range(l1)]

# initialization
for i in range(l2):
    if s1[0] in s2[:i+1]:
        dp[0][i] = 1

for i in range(l1):
    if s2[0] in s1[:i+1]:
        dp[i][0] = 1

# dp
for i in range(1,l1):
    for j in range(1,l2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

