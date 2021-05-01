# https://www.acmicpc.net/problem/1080

n,m = list(map(int, input().split()))
change = [list(map(int, list(input()))) for _ in range(n)]
final = [list(map(int, list(input()))) for _ in range(n)]

def convert(x,y,arr):
    for i in range(x,x+3):
        for j in range(y,y+3):
            arr[i][j]=1-arr[i][j]
cnt=0
for i in range(n-2):
    for j in range(m-2):
        if change[i][j]!=final[i][j]:
            convert(i,j,change)
            cnt+=1

flag = 0
for i in range(n):
    for j in range(m):
        if change[i][j]!=final[i][j]:
            flag=1
if flag:
    print(-1)
else:
    print(cnt)


