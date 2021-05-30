# https://www.acmicpc.net/problem/2589
from collections import deque

m,n = list(map(int, input().split()))
arr = []
q = deque()
direction = [(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(m):
    arr.append(list(input()))
for i in range(m):
    for j in range(n):
        if arr[i][j] == 'L':
            q.append
        arr[i][j] = 'W'
print(ans)