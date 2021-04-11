# https://www.acmicpc.net/problem/1010

t = int(input())
for _ in range(t):
    n,m = list(map(int, input().split()))

    ans = 1
    for i in range(n):
        ans *= m-i

    for i in range(1,n+1):
        ans //= i

    print(ans)