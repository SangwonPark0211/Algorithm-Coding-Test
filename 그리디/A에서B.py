# https://www.acmicpc.net/problem/16953
from collections import deque

a, b = list(map(int, input().split()))
q = deque()
visit = set()
visit.add(a)
q.append((a,0))
flag = 0
while q:
    x, c = q.popleft()
    if x==b:
        print(c+1)
        flag = 1
        break
    candidate1, candidate2 = x*2, int(str(x)+'1')
    if candidate1 not in visit and candidate1 <= b:
        q.append((candidate1, c+1))
        visit.add(candidate1)
    if candidate2 not in visit and candidate2 <= b:
        q.append((candidate2, c+1))
        visit.add(candidate1)
if flag==0:
    print(-1)