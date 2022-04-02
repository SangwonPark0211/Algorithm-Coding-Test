# https://www.acmicpc.net/problem/13549
import heapq

N, K = map(int, input().split())
visit = [0]*100001
hq = []
heapq.heappush(hq, (0,N))
visit[N] = 1
while hq:
    t, pos = heapq.heappop(hq)
    if pos == K:
        print(t)
        break
    if 0<=2*pos<=100000 and visit[2*pos] == 0:
        heapq.heappush(hq, (t, 2*pos))
        visit[2*pos] = 1
    if 0<=pos-1<=100000 and visit[pos-1] == 0:
        heapq.heappush(hq, (t+1,pos-1))
        visit[pos-1] = 1
    if 0<=pos+1<=100000 and visit[pos+1] == 0:
        heapq.heappush(hq, (t+1,pos+1))
        visit[pos+1] = 1
    

