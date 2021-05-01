# https://www.acmicpc.net/problem/13305

n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

ans = 0
minval = city[0]
for i in range(n-1):
    if minval>city[i]:
        minval=city[i]
    ans+=minval*road[i]
print(ans)