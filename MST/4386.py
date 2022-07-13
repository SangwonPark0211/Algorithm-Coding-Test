import sys, heapq
input = sys.stdin.readline

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

n = int(input())
pos = [tuple(map(float,input().split())) for _ in range(n)]
# 인접 리스트 생성
link = [[] for _ in range(n)]
for i in range(n):
    x1,y1 = pos[i]
    for j in range(n):
        if i==j:
            continue
        x2,y2 = pos[j]
        link[i].append((j,dist(x1,y1,x2,y2)))

# Prim
visit = [False] * n
hq = [(0,0)]
cnt,ans = n,0
while cnt:
    curDist,curNode = heapq.heappop(hq)
    if visit[curNode]:
        continue
    
    cnt -= 1
    visit[curNode] = True
    ans += curDist
    for toNode,toDist in link[curNode]:
        if visit[toNode]:
            continue
        heapq.heappush(hq,(toDist,toNode))
print(ans)