# https://www.acmicpc.net/problem/2003

N, K = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, 1
cnt = 0
while r <= N and l <= r:
    temp = nums[l:r]
    temp_sum = sum(temp)
    
    if temp_sum == K:
        cnt += 1
        r += 1
    elif temp_sum < K:
        r += 1
    else:
        l += 1
print(cnt)