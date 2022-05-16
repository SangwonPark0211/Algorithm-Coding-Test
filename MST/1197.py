# https://www.acmicpc.net/problem/1197
import sys
input = sys.stdin.readline

def getParent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = getParent(parent[x])
        return parent[x]

# 합치기
def unionParent(x, y):
    x_p, y_p = getParent(x), getParent(y)
    if x_p < y_p:
        parent[y_p] = parent[x_p]
    else:
        parent[x_p] = parent[y_p]

# 같은 부모를 갖는지 확인
def isSameParent(x, y):
    if getParent(x) == getParent(y):
        return True
    else:
        return False

V, E = map(int, input().split())
parent = [i for i in range(V)]
g = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    g.append((cost, a-1, b-1))
    
# cost 기준 오름차순으로 정렬
g.sort()
cnt = 0
total_cost = 0
for cost, a, b in g:
    if cnt == V-1:
        break
    # 사이클 생기면 continue
    if isSameParent(a, b):
        continue
    # 사이클 안생기면 total_cost에 더해주기
    else:
        total_cost += cost
        cnt += 1
        unionParent(a, b)
print(total_cost)
        



