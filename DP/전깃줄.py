# https://www.acmicpc.net/problem/2565

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key = lambda x : x[0])

arr2 = [y for x,y in arr]
dp = [1 for _ in range(n)]

for i in range(1,n):
    front = 0
    for j in range(i):
        if arr2[i] > arr2[j]:
            front = max(front, dp[j])
    dp[i] += front

print(n - max(dp))