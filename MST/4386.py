# https://www.acmicpc.net/problem/4386

import sys,heapq
input = sys.stdin.readline

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

n = int(input())
pos = [tuple(map(float,input().split())) for _ in range(n)]

link = [[] for _ in range(n)]
for i in range(n):
    x1,y1 = pos[i]
    for j in range(n):
        if i==j:
            continue
        x2,y2 = pos[j]
        link[i].append((j,dist(x1,y1,x2,y2)))

# Prim
cnt = n
ans = 0
hq = [(0,0)]    # (weight, node)
visit = [False]*n
while cnt:
    curDist, curNode = heapq.heappop(hq)
    if visit[curNode]:
        continue

    ans += curDist
    cnt -= 1
    visit[curNode] = True
    for toNode, toDist in link[curNode]:
        if visit[toNode]:
            continue
        heapq.heappush(hq, (toDist, toNode))
    
print(ans)









