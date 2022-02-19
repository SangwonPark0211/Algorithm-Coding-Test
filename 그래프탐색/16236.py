# https://www.acmicpc.net/problem/16236
from collections import deque

def bfs(y,x):
    global N, cur_size, eaten, cur_pos, time, call_mom
    visit = set()
    q = deque()
    q.append((0, y, x))
    visit.add((y,x))
    eatable = []
    while q:
        distance, cur_y, cur_x = q.popleft()
        for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
            ny, nx = cur_y+dy, cur_x+dx
            if 0<=ny<N and 0<=nx<N and (ny,nx) not in visit and 0 <= arr[ny][nx] <= cur_size:
                if 0 < arr[ny][nx] < cur_size:
                    eatable.append((distance+1, ny, nx))
                q.append((distance+1, ny, nx))
                visit.add((ny,nx))
    if len(eatable) == 0:
        call_mom = True
        return
    eatable = sorted(eatable, key=lambda x:(x[0],x[1],x[2]))
    arr[eatable[0][1]][eatable[0][2]] = 0
    eaten += 1
    if eaten == cur_size:
        cur_size += 1
        eaten = 0
    cur_pos = (eatable[0][1], eatable[0][2])
    time += eatable[0][0]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
eaten = 0
cur_size = 2
cur_pos = (0,0)
time = 0
call_mom = False

for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            cur_pos = (i,j)
            arr[i][j] = 0
while not call_mom:
    bfs(cur_pos[0], cur_pos[1])

print(time)





