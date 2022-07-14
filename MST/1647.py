# https://www.acmicpc.net/problem/1647
import sys, heapq
input = sys.stdin.readline

house, road = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(road)]
link = [[] for _ in range(house)]
for x,y,cost in pos:
    link[x-1].append((y-1,cost))
    link[y-1].append((x-1,cost))

ans = 0
cnt = house
hq = [(0,0)] # (cost, node)
visit = [False]*(house+1)
max_cost = 0
while cnt:
    curDist, curNode = heapq.heappop(hq)
    if visit[curNode]:
        continue
    visit[curNode] = True
    cnt -= 1
    ans += curDist
    max_cost = max(max_cost, curDist)
    for toNode, toDist in link[curNode]:
        if visit[toNode]:
            continue
        heapq.heappush(hq, (toDist, toNode))
print(ans-max_cost)