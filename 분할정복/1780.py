# https://www.acmicpc.net/problem/1780

ans = {-1:0, 0:0, 1:0}

def decompose(n, y, x):
    if n == 1:
        ans[arr[y][x]] += 1
        return

    flag = True
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != arr[y][x]:
                flag = False
                break
    
    if flag is True:
        ans[arr[y][x]] += 1
    else:
        new_n = n // 3
        decompose(new_n, y, x)
        decompose(new_n, y, x+new_n)
        decompose(new_n, y, x+2*new_n)
        decompose(new_n, y+new_n, x)
        decompose(new_n, y+new_n, x+new_n)
        decompose(new_n, y+new_n, x+2*new_n)
        decompose(new_n, y+2*new_n, x)
        decompose(new_n, y+2*new_n, x+new_n)
        decompose(new_n, y+2*new_n, x+2*new_n)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
decompose(N, 0, 0)
print(ans[-1])
print(ans[0])
print(ans[1])