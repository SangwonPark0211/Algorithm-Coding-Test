# https://www.acmicpc.net/problem/10162

t = int(input())
timer = [300, 60, 10]
ans = [0,0,0]
for i in range(3):
    if timer[i]>t:
        continue
    else:
        ans[i] += t//timer[i]
        t = t%timer[i]
if t==0:
    for i in range(3):
        print(ans[i], end=' ')
else:
    print(-1)