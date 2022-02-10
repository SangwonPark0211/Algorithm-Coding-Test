# https://www.acmicpc.net/problem/1992

def decompose(n, y, x):
    if n == 1:
        print(arr[y][x], end='')
        return
    flag = True
    for i in range(y,y+n):
        for j in range(x,x+n):
            if arr[i][j] != arr[y][x]:
                flag = False
                break
    if flag is True:
        print(arr[y][x], end='')
    else:
        half_n = n//2
        print('(', end='')
        decompose(half_n, y, x)
        decompose(half_n, y, x+half_n)    
        decompose(half_n, y+half_n, x)
        decompose(half_n, y+half_n, x+half_n)
        print(')', end='')
    
N = int(input())
arr = [input() for _ in range(N)]
decompose(N, 0, 0)