# https://www.acmicpc.net/problem/14502
import copy

# 벽을 세울 3곳의 조합(combination)을 구하는 함수
def make_3comb(comb, zero):
    zero_len = len(zero)
    for i in range(zero_len-2):
        for j in range(i+1, zero_len-1):
            for k in range(j+1,zero_len):
                comb.append((zero[i][0], zero[i][1], zero[j][0], zero[j][1], zero[k][0], zero[k][1]))

# dfs로 바이러스 퍼지는 것 구현하는 함수
def dfs(x,y,visit,temp_arr):
    if (x,y) in visit:
        return
    visit.add((x,y))
    temp_arr[x][y] = 2
    direction = ((-1,0),(1,0),(0,-1),(0,1))
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<m:
            if temp_arr[nx][ny]==0:
                dfs(nx,ny,visit,temp_arr)

# 안전영역 카운트하는 함수
def zero_cnt(temp_arr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j]==0:
                cnt += 1
    return cnt


n,m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
zero = []
comb = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            zero.append((i,j))
make_3comb(comb, zero)
ans = 0
for x1,y1,x2,y2,x3,y3 in comb:
    temp_arr = copy.deepcopy(arr)
    temp_arr[x1][y1], temp_arr[x2][y2], temp_arr[x3][y3] = 1, 1, 1
    visit = set()
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j]==2 and (i,j) not in visit:
                dfs(i,j,visit,temp_arr)
    ans = max(ans, zero_cnt(temp_arr))

print(ans)
