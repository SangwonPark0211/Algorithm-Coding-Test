# https://www.acmicpc.net/problem/10026
import copy
import sys
# 런타임 에러 방지
sys.setrecursionlimit(100000)

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))
direction = ((1,0),(-1,0),(0,1),(0,-1))

def not_rgblind(x, y, arr1, visit1):
    visit1.add((x,y))
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<n:
            if (nx,ny) not in visit1 and arr1[nx][ny]==arr1[x][y]:
                not_rgblind(nx,ny,arr1,visit1)

def rgblind(x, y, arr2, visit2):
    visit2.add((x,y))
    same = (('R','G'),('G','R'))
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<n:
            if (nx,ny) not in visit2:
                if (arr2[x][y]==arr2[nx][ny]) or ((arr2[x][y],arr2[nx][ny]) in same):
                    rgblind(nx,ny,arr2,visit2)

notblind, blind = 0, 0
visit1, arr1 = set(), copy.deepcopy(arr)
visit2, arr2 = set(), copy.deepcopy(arr)

for i in range(n):
    for j in range(n):
        if (i,j) not in visit1:
            notblind += 1
            not_rgblind(i,j, arr1, visit1)
for i in range(n):
    for j in range(n):
        if (i,j) not in visit2:
            blind += 1
            rgblind(i,j,arr2,visit2)

print(notblind, blind)