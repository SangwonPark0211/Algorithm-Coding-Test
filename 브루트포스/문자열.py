# https://www.acmicpc.net/problem/1120

def cal_diff(x,y):
    cnt = 0
    for i in range(len(x)):
        if x[i]!=y[i]:
            cnt += 1
    return cnt

a, b = input().split()
len_diff = len(b)-len(a)
comb = []
for i in range(len_diff+1):
    comb.append((i, len_diff-i))

ans = len(b)
for i,j in comb:
    ans = min(ans, cal_diff(a,b[i:len(b)-j]))
print(ans)