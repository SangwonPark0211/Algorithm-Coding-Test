# https://www.acmicpc.net/problem/2583
import sys
sys.setrecursionlimit(10000)

area = 0
arr = []
visit = set()

def dfs(x, y):
    global area, arr, visit
    if (x,y) in visit:
        return
    visit.add((x,y))
    area += 1
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    for dx,dy in direction:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if (nx,ny) not in visit and arr[nx][ny]==0:
                dfs(nx, ny)


n, m, k = list(map(int, input().split()))
arr = [[0 for _ in range(m)] for _ in range(n)]
retangle = []
for _ in range(k):
    retangle.append(list(map(int, input().split())))

for x1,y1,x2,y2 in retangle:
    for i in range(y1, y2):
        for j in range(x1,x2):
            arr[i][j] = 1
ans = []
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and (i,j) not in visit:
            dfs(i, j)
            cnt += 1
            ans.append(area)
            area = 0
print(cnt)
ans.sort()
for a in ans:
    print(a, end=' ')