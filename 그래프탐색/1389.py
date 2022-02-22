# https://www.acmicpc.net/problem/1389
import sys
from math import inf
N, M = map(int, sys.stdin.readline().split())
arr = [[inf]*N for _ in range(N)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1][j-1] = 1
    arr[j-1][i-1] = 1
for i in range(N):
    arr[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
kevin_num, ans = sum(arr[0]), 0
for i in range(1, N):
    if sum(arr[i]) < kevin_num:
        kevin_num = sum(arr[i])
        ans = i
    elif sum(arr[i]) == kevin_num:
        if i < ans:
            ans = i

print(ans+1)

