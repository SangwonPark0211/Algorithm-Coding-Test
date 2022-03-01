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
    if pos==100:
        print(cnt)
        break
    for i in range(1,7):
        new_p = pos+i
        if new_p <= 100 and visit[new_p] == 0:
            visit[new_p] = 1
            if new_p in snake:
                q.append((snake[new_p],cnt+1))
            elif new_p in ladder:
                q.append((ladder[new_p],cnt+1))
            else:
                q.append((new_p,cnt+1))
            