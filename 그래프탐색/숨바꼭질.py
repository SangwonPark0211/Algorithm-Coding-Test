# https://www.acmicpc.net/problem/1697
from collections import deque

n, k = list(map(int, input().split()))
q = deque()
q.append((n,0)) # (position, time)
visit = set()
visit.add(n)

while q:
    pos, time = q.popleft()
    if pos == k:
        print(time)
        break
    if pos<0 or pos>100000:
        continue
    if pos-1 not in visit:
        q.append((pos-1, time+1))
        visit.add(pos-1)
    if pos+1 not in visit:
        q.append((pos+1, time+1))
        visit.add(pos+1)
    if pos*2 not in visit:
        q.append((pos*2, time+1))
        visit.add(pos*2)
