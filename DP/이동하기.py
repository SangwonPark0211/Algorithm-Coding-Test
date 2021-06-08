# https://www.acmicpc.net/problem/11048

r, c = list(map(int, input().split()))
a = []
for _ in range(r):
    a.append(list(map(int, input().split())))

for i in range(1,c):
    a[0][i] += a[0][i-1]
for i in range(1,r):
    a[i][0] += a[i-1][0]

for i in range(1,r):
    for j in range(1,c):
        a[i][j] += max(a[i-1][j-1], max(a[i-1][j], a[i][j-1]))

print(a[-1][-1])