# https://www.acmicpc.net/problem/2467

N = int(input())
arr = list(map(int, input().split()))
l, r = 0, N-1
ans = [arr[-2], arr[-1]]
while l < r:
    s = arr[l] + arr[r]
    if s == 0:
        ans[0] = arr[l]
        ans[1] = arr[r]
        break
    elif s < 0:
        if abs(s) < abs(sum(ans)):
            ans[0], ans[1] = arr[l], arr[r]
        l += 1
    else:
        if abs(s) < abs(sum(ans)):
            ans[0], ans[1] = arr[l], arr[r]
        r -= 1
print(ans[0], ans[1])
