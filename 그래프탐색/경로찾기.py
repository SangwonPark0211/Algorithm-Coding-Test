# https://www.acmicpc.net/problem/11403
from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))



for k in range(n):
    for i in range(n):
        for j in range(n):
            print((i,k), (k,j))
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
        
    
        
