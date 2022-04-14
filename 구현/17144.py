# https://www.acmicpc.net/problem/17144

import sys
input = sys.stdin.readline
import copy

R, C, T = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(map(int, input().strip().split())))
circulator = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            circulator.append([i,j])

def diff():
    dust_pos = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 1:
                dust_pos.append([i,j,arr[i][j]])
    for r,c,d in dust_pos:
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr, nc = r + dr, c + dc
            if 0<=nr<R and 0<=nc<C and arr[nr][nc]!=-1:
                arr[nr][nc] += d//5
                arr[r][c] -= d//5

def move():
    temp = copy.deepcopy(arr)
    
    # upper
    y1, x1 = circulator[0]
    arr[y1][1] = 0
    for i in range(2, C):
        arr[y1][i] = temp[y1][i-1]
    for i in range(y1-1, -1, -1):
        arr[i][C-1] = temp[i+1][C-1]
    for i in range(C-2, -1, -1):
        arr[0][i] = temp[0][i+1]
    for i in range(1, y1):
        arr[i][0] = temp[i-1][0]

    # lower
    y2, x2 = circulator[1]
    arr[y2][1] = 0
    for i in range(2, C):
        arr[y2][i] = temp[y2][i-1]
    for i in range(y2+1, R):
        arr[i][C-1] = temp[i-1][C-1]
    for i in range(C-2, -1, -1):
        arr[R-1][i] = temp[R-1][i+1]
    for i in range(R-2, y2, -1):
        arr[i][0] = temp[i+1][0]

for _ in range(T):
    diff()
    move()
ans = 0
for i in range(R):
    ans += sum(arr[i])
print(ans+2)

