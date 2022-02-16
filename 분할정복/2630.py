# https://www.acmicpc.net/problem/2630

ans = {'0':0, '1':0}

def decompose(n, y, x):
    if n==1:
        ans[arr[y][x]] += 1
        return
    
    flag = True
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j]!=arr[y][x]:
                flag = False
                break
        if flag == False:
            break
    
    if flag==True:
        ans[arr[y][x]] += 1
    else:
        nn = n//2
        decompose(nn, y, x)
        decompose(nn, y, x+nn)
        decompose(nn, y+nn, x)
        decompose(nn, y+nn, x+nn)

N = int(input())
arr = [input().split() for _ in range(N)]
decompose(N,0,0)
print(ans['0'])
print(ans['1'])

