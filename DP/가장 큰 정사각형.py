# https://www.acmicpc.net/problem/1915

n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))

for i in range(1,n):
    for j in range(1,m):
        if arr[i][j]==1:
            arr[i][j] = min(arr[i-1][j], min(arr[i][j-1], arr[i-1][j-1])) + 1

ans = 0
for l in arr:
    ans = max(ans, max(l))
print(ans*ans)
