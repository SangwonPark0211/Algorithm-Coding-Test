# https://www.acmicpc.net/problem/1744

n = int(input())
arr = []
ans = 0
for _ in range(n):
    arr.append(int(input()))
arr.sort()
neg, pos, zero_one = [], [], [] 
for i in range(n):
    if arr[i]>1:
        pos.append(arr[i])
    elif arr[i]<0:
        neg.append(arr[i])
    else:
        zero_one.append(arr[i])
pos.sort(reverse=True)
if len(pos)%2==0:
    for i in range(0,len(pos)-1,2):
        ans += pos[i]*pos[i+1]
else:
    for i in range(0,len(pos)-2,2):
        ans += pos[i]*pos[i+1]
    ans += pos[-1]
neg.sort()
if len(neg)%2==0:
    for i in range(0,len(neg)-1,2):
        ans += neg[i]*neg[i+1]
else:
    for i in range(0,len(neg)-2,2):
        ans += neg[i]*neg[i+1]
    if 0 not in zero_one:
        ans += neg[-1]
ans += sum(zero_one)
print(ans)

