# https://www.acmicpc.net/problem/2745

num, base = input().split()
base = int(base)

ans = 0
l = len(num)
for i in range(len(num)):
    x = num[i]
    if ord('0')<=ord(x)<=ord('9'):
        ans += int(x) * (base**(l-1-i))
    else:
        ans += (ord(x)-ord('A')+10) * (base**(l-1-i))
print(ans)
