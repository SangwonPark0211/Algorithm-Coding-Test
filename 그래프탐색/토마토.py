# https://www.acmicpc.net/problem/7569
from collections import deque

m,n,h = list(map(int, input().split()))
arr = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    arr.append(temp)

q = deque()
visit = set()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i,j,k))
                visit.add((i,j,k))

direction = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
l = len(q)
day = 0
while q:
    for _ in range(l):
        x,y,z = q.popleft()
        arr[x][y][z] = 1
        for dx,dy,dz in direction:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                if arr[nx][ny][nz] == 0 and (nx,ny,nz) not in visit:
                    q.append((nx,ny,nz))
                    visit.add((nx,ny,nz))
    day += 1
    l = len(q)

def main(arr, day, h, n):
    for i in range(h):
        for j in range(n):
            if 0 in arr[i][j]:
                print(-1)
                return
    print(day-1)

main(arr, day, h, n)



