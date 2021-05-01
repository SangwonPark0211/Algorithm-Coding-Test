# https://www.acmicpc.net/problem/1715
import heapq
n = int(input())
card=[]
for _ in range(n):
    heapq.heappush(card, int(input()))
if n==1:
    print(0)
else:
    ans = 0
    for i in range(n-1):
        prev = heapq.heappop(card)
        cur = heapq.heappop(card)
        s = prev+cur
        ans += s
        heapq.heappush(card, s)
    print(ans)
        

