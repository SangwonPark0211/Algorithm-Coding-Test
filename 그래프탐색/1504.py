# https://www.acmicpc.net/problem/1504
import sys
input = sys.stdin.readline
import heapq
inf = sys.maxsize

N, E = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
v1, v2 = map(int, input().split())


def dijkstra(start):
    dp = [inf for _ in range(N+1)]
    dp[start] = 0
    hq = []
    heapq.heappush(hq, [0,start])
    while hq:
        w, c = heapq.heappop(hq)
        for n_n, n_w in arr[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heapq.heappush(hq, [wei, n_n])
    return dp

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
ans = min(one[v1]+v1_[v2]+v2_[N], one[v2]+v2_[v1]+v1_[N])
print(ans if ans<inf else -1)
