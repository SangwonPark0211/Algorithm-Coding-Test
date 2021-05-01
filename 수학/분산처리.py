# https://www.acmicpc.net/problem/1009

# t = int(input())
# num_seq = {0:[0], 1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 5:[5], 6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1]}
# for _ in range(t):
#     a,b = list(map(int, input().split()))
#     a %= 10
#     if a in (1,5,6):
#         print(a)
#     elif a==0:
#         print(10)
#     else:
#         order = b % len(num_seq[a])
#         if order==0:
#             print(num_seq[a][-1])
#         else:
#             print(num_seq[a][order-1])
import sys
t = int(sys.stdin.readline())
for i in range(t):


    a, b = map(int, sys.stdin.readline().split())
    temp = 1
    result_list = []
    for _ in range(b):
        temp *= a
        temp %= 10
        if temp in result_list:
            break
        result_list.append(temp)
    result = result_list[b%len(result_list) - 1]
    if result == 0:
        print(10)
    else:
        print(result)