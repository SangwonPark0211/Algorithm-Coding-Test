# https://www.acmicpc.net/problem/20040
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def getParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent[x])
        return parent[x]

def unionParent(x,y):
    x_parent = getParent(x)
    y_parent = getParent(y)
    if x_parent < y_parent:
        parent[x_parent] = y_parent
    else:
        parent[y_parent] = x_parent

def isSameParent(x,y):
    if getParent(x) == getParent(y):
        return True
    else:
        return False

node, turn = map(int, input().split())
edge = []
for _ in range(turn):
    edge.append((tuple(map(int, input().split()))))
parent = [i for i in range(node)]
cnt = 0
done = False
for x,y in edge:
    cnt += 1
    if isSameParent(x,y):
        print(cnt)
        done = True
        break
    unionParent(x,y)
if not done:
    print(0)
