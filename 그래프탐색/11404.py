# https://www.acmicpc.net/problem/11404

import sys
from math import inf
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

cost = [[inf for _ in range(n)] for _ in range(n)]
for _ in range(m):
    start, end, w = map(int, input().split())
    if cost[start-1][end-1] > w:
        cost[start-1][end-1] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j or i==k or j==k:
                continue
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

for i in range(n):
    for j in range(n):
        if cost[i][j]==inf:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()
