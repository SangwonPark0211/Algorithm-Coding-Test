# https://www.acmicpc.net/problem/2573
import copy
from collections import deque

n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def melt():
    n_arr = copy.deepcopy(arr)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i][j] == 0:
                continue
            cnt = 0
            if arr[i-1][j] == 0:
                cnt += 1
            if arr[i+1][j] == 0:
                cnt += 1
            if arr[i][j-1] == 0:
                cnt += 1
            if arr[i][j+1] == 0:
                cnt += 1

            if arr[i][j] - cnt <= 0:
                n_arr[i][j] = 0
            else:
                n_arr[i][j] -= cnt
    return n_arr

def bfs(x, y, visit):
    q = deque()
    q.append((x,y))
    visit.add((x,y))
    while q:
        s_x, s_y = q.popleft()
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in direction:
            nx = s_x + dx
            ny = s_y + dy
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]!=0 and (nx,ny) not in visit:
                q.append((nx,ny))
                visit.add((nx,ny))

year = 0
while True:
    component = 0
    visit = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and (i,j) not in visit:
                component += 1
                bfs(i, j, visit)
    if component >= 2:
        print(year)
        break
    if component == 0:
        print(0)
        break
    arr = melt()
    year += 1

