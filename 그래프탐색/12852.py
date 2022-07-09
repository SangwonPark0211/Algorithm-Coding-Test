# https://www.acmicpc.net/problem/12852

from collections import deque
import copy

n = int(input())
visit = [0] * (10**6+1)
q = deque()
q.append((n, [n]))
while q:
    pos, history = q.popleft()
    if pos == 1:
        print(len(history)-1)
        history = list(map(str, history))
        print(' '.join(history))
        break
    if pos % 2 == 0 and visit[pos//2] == 0:
        q.append((pos//2, history[:]+[pos//2]))
        visit[pos//2] = 1
    if pos % 3 == 0 and visit[pos//3] == 0:
        q.append((pos//3, history[:]+[pos//3]))
        visit[pos//3] = 1
    if visit[pos-1] == 0:
        q.append((pos-1, history[:]+[pos-1]))
        visit[pos-1] = 1

