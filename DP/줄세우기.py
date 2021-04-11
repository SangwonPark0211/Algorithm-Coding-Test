# https://www.acmicpc.net/problem/2631

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [1 for _ in range(n)]
for i in range(1,n):
    front = 0
    for j in range(i):
        if arr[j] < arr[i]:
            front = max(front, dp[j])
    dp[i] += front
print(n-max(dp))