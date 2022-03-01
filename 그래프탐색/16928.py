# https://www.acmicpc.net/problem/16928

import sys
from collections import deque

ladder, snake = {}, {}
q = deque()
M, N = map(int, sys.stdin.readline().split())
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    ladder[start] = end
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    snake[start] = end

visit = [0]*101
q.append((1,0))   # (position, cnt)
visit[1] = 1
while q:
    pos, cnt = q.popleft()
    print(pos, cnt)
    if pos==100:
        print(cnt)
        break
    if pos in ladder:
        q.append((ladder[pos],cnt))
        visit[ladder[pos]] = 1
        continue
    elif pos in snake:
        continue
    else:
        for i in range(1,7):
            if pos+i <= 100 and visit[pos+i] == 0:
                q.append((pos+i,cnt+1))
                visit[pos+i] = 1





