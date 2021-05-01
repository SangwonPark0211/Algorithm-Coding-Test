# https://www.acmicpc.net/problem/7562
from collections import deque
t = int(input())
direction = [[-2,-1],[-1,-2],[-2,1],[-1,2],[2,-1],[1,-2],[2,1],[1,2]]
for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))
    q = deque()
    visit = set()
    q.append((start[0],start[1],0))
    visit.add((start[0],start[1]))
    while q:
        x,y,c = q.popleft()
        # print(x,y,c)
        if [x,y]==[finish[0],finish[1]]:
            print(c)
            break
        for dx,dy in direction:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<n and (nx,ny) not in visit:
                visit.add((nx,ny))
                q.append((nx,ny,c+1))
