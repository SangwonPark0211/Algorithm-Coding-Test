# https://www.acmicpc.net/problem/3109
def traverse(x, y):
    arr[x][y] = '1'
    if y == c-1:
        return True

    dirs = [(-1,1),(0,1),(1,1)]
    for dx,dy in dirs:
        nx,ny = x+dx, y+dy
        if 0<=nx<r and 0<=ny<c and arr[nx][ny] == '.':
            if traverse(nx, ny):
                return True

    return False

r, c = list(map(int, input().split()))
arr = []
for _ in range(r):
    arr.append(list(input()))
ans = 0
for i in range(r):
    if traverse(i,0):
        ans += 1

print(ans)


