# https://www.acmicpc.net/problem/9663

def backtracking(selected, order):
    global N, ans
    if order==N:
        ans += 1
        return
    for i in range(N):
        new_pos = (order,i)
        flag = False
        for y,x in selected:
            # selected안의 모든 위치들과 행, 열, 대각선 방향에서 겹치면
            if order==y or i==x or abs(order-y)==abs(i-x):
                flag = True
                break
        if flag is False:
            backtracking(selected+[(order,i)], order+1)

global ans, N
ans = 0
N = int(input())
for i in range(N):
    backtracking([(0,i)], 1)
print(ans)