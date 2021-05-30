# https://www.acmicpc.net/problem/1202

n, k = list(map(int,input().split()))
jewelry = []
for _ in range(n):
    m, p = list(map(int, input().split()))
    jewelry.append((p,m))
jewelry.sort(key=lambda x : (-x[0], x[1]))
bag = []
for _ in range(k):
    bag.append(int(input()))
bag.sort()
ans = 0
for p, m in jewelry:
    if len(bag)==0:
        break
    for i in range(len(bag)):
        if bag[i]>=m:
            del bag[i]
            ans += p
            break
print(ans)